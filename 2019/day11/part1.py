from dataclasses import dataclass
from defaultlist import defaultlist
from enum import IntEnum

with open('input.txt') as f:
    inp = [int(x) for x in f.read().split(',')]


class Colors(IntEnum):
    BLACK = 0
    WHITE = 1


class Direction(IntEnum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3


class Mode(IntEnum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class OpCode(IntEnum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    ADJUST_RELATIVE_BASE = 9
    TERMINATE = 99


@dataclass
class Location:
    x: int
    y: int
    color: Colors


class Instruction:
    def __init__(self, client, data):
        self.client = client
        self.program = client.program
        data = str(data)
        self.opcode = OpCode(int(data[-2:]))
        self.modes = defaultlist(lambda: Mode(0)) + [Mode(int(x)) for x in reversed(data[:-2])]

    def read(self, pos):
        if self.modes[pos] == Mode.POSITION:
            return self.program[self.program[self.client.cursor + pos + 1]]
        elif self.modes[pos] == Mode.IMMEDIATE:
            return self.program[self.client.cursor + pos + 1]
        elif self.modes[pos] == Mode.RELATIVE:
            return self.program[self.program[self.client.cursor + pos + 1] + self.client.relative_base]

    def write(self, pos, val):
        if self.modes[pos] == Mode.POSITION:
            self.program[self.program[self.client.cursor + pos + 1]] = val
        elif self.modes[pos] == Mode.IMMEDIATE:
            raise NotImplementedError('Immediate mode is unsupported for writes')
        elif self.modes[pos] == Mode.RELATIVE:
            self.program[self.program[self.client.cursor + pos + 1] + self.client.relative_base] = val


class IntCode:
    def __init__(self, program):
        self.program = defaultlist(lambda: 0) + program
        self.cursor = 0
        self.relative_base = 0
        self.output_count = 0

    def run(self):
        while True:
            instruction = Instruction(self, self.program[self.cursor])
            if instruction.opcode == OpCode.TERMINATE:
                break
            self.cursor += getattr(self, 'execute_' + instruction.opcode.name.lower())(instruction)

    def execute_add(self, instruction):
        instruction.write(2, instruction.read(0) + instruction.read(1))
        return 4

    def execute_multiply(self, instruction):
        instruction.write(2, instruction.read(0) * instruction.read(1))
        return 4

    def execute_input(self, instruction):
        try:
            color = list(filter(lambda x: [x.x, x.y] == cursor[:2], painting))[-1].color
        except IndexError:
            color = Colors.BLACK
        instruction.write(0, color.value)
        return 2

    def execute_output(self, instruction):
        if self.output_count == 0:
            painting.append(Location(*cursor[:2], Colors(instruction.read(0))))
            self.output_count += 1
        elif self.output_count == 1:
            cursor[2] = Direction(instruction.read(0))
            move()
            self.output_count = 0

        return 2

    def execute_jump_if_true(self, instruction):
        if instruction.read(0) == 0:
            cursor_change = 3
        else:
            cursor_change = instruction.read(1) - self.cursor
        return cursor_change

    def execute_jump_if_false(self, instruction):
        if instruction.read(0) == 0:
            cursor_change = instruction.read(1) - self.cursor
        else:
            cursor_change = 3
        return cursor_change

    def execute_less_than(self, instruction):
        if instruction.read(0) < instruction.read(1):
            instruction.write(2, 1)
        else:
            instruction.write(2, 0)
        return 4

    def execute_equals(self, instruction):
        if instruction.read(0) == instruction.read(1):
            instruction.write(2, 1)
        else:
            instruction.write(2, 0)
        return 4

    def execute_adjust_relative_base(self, instruction):
        self.relative_base += instruction.read(0)

        return 2


def move():
    if cursor[2] == Direction.LEFT:
        cursor[3] += 90
    elif cursor[2] == Direction.RIGHT:
        cursor[3] -= 90

    cursor[3] %= 360

    if cursor[3] == 90:
        cursor[0] -= 1
    elif cursor[3] == 180:
        cursor[1] += 1
    elif cursor[3] == 270:
        cursor[0] += 1
    elif cursor[3] in (360, 0):
        cursor[1] -= 1
    else:
        print(cursor[3], 'non')


painting = [Location(0, 0, Colors.BLACK)]
cursor = [0, 0, Direction.UP, 0]  # x, y, direction, degrees
IntCode(inp).run()
count = set()
for i in painting:
    count.add((i.x, i.y))

print(len(count))
