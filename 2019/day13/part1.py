from dataclasses import dataclass
from defaultlist import defaultlist
from enum import IntEnum

with open('input.txt') as f:
    inp = [int(x) for x in f.read().split(',')]


@dataclass()
class Coordinates:
    x: int
    y: int

    def __hash__(self):
        return hash(f'{self.x},{self.y}')


class Direction(IntEnum):
    NEUTRAL = 0
    LEFT = -1
    RIGHT = 1


class TileType(IntEnum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    HORIZONTAL_PADDLE = 3
    BALL = 4


@dataclass()
class Tile:
    x: int
    y: int
    type_id: int

    @property
    def type_(self):
        return TileType(self.type_id)


class Game(dict):
    @property
    def paddle(self):
        for k in game:
            if game[k].type_ == TileType.HORIZONTAL_PADDLE:
                return game[k]

    @property
    def width(self):
        w = 0
        for k in game:
            if k.x > w:
                w = k.x
        return w

    @property
    def height(self):
        h = 0
        for k in game:
            if k.y > h:
                h = k.y
        return h


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

    def __repr__(self):
        return '<Instruction opcode={0.opcode}>'.format(self)


class IntCode:
    def __init__(self, program):
        self.program = defaultlist(lambda: 0) + program
        self.cursor = 0
        self.relative_base = 0

        self.output_count = 0
        self.outputs = []

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
        # instruction.write(0, self.id)
        # for i in game.blocks
        # raise NotImplementedError
        if game.paddle.x < game.width - 10:
            instruction.write(0, Direction.LEFT)
        elif game.paddle.x > 10:
            instruction.write(0, Direction.RIGHT)
        return 2

    def execute_output(self, instruction):
        self.outputs.append(instruction.read(0))
        self.output_count += 1

        if self.output_count % 3 == 0:
            if self.outputs[:2] == [-1, 0]:
                print('score', self.outputs[2])
            else:
                game[Coordinates(*self.outputs[:2])] = (Tile(*self.outputs))
                self.outputs = []

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


game = Game()
inp[0] = 2  # play for free
IntCode(inp).run()
