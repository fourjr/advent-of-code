from enum import IntEnum

with open('input.txt') as f:
    inp = [int(x) for x in f.read().split(',')]


def format_instruction(instruction, length):
    instruction = str(instruction)
    while len(instruction) < length:
        instruction = '0' + instruction

    return [Mode(int(x)) for x in reversed(instruction)]


class Mode(IntEnum):
    POSITION = 0
    IMMEDIATE = 1


class OpCode(IntEnum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8


class IntCode:
    def __init__(self, program, id_):
        self.program = program
        self.id = id_
        self.cursor = 0

    def get_param(self, mode, value):
        if mode == Mode.POSITION:
            return self.program[value]
        elif mode == Mode.IMMEDIATE:
            return value

    def run(self):
        while int(str(self.program[self.cursor])[-2:]) != 99:
            opcode = OpCode(int(str(inp[self.cursor])[-2:]))
            self.cursor += getattr(self, 'execute_' + opcode.name.lower())(str(self.program[self.cursor])[:-2])  # paramter is the opcode minus off last 2 digits

    def execute_add(self, instruction):
        instructions = format_instruction(instruction, 3)
        self.program[inp[self.cursor + 3]] = self.get_param(instructions[0], self.program[self.cursor + 1]) + self.get_param(instructions[1], self.program[self.cursor + 2])

        return 4

    def execute_multiply(self, instruction):
        instructions = format_instruction(instruction, 3)
        self.program[inp[self.cursor + 3]] = self.get_param(instructions[0], self.program[self.cursor + 1]) * self.get_param(instructions[1], self.program[self.cursor + 2])

        return 4

    def execute_input(self, instruction):
        self.program[self.program[self.cursor + 1]] = self.id

        return 2

    def execute_output(self, instruction):
        instructions = format_instruction(instruction, 1)
        print(self.cursor, self.get_param(instructions[0], self.program[self.cursor + 1]))

        return 2

    def execute_jump_if_true(self, instruction):
        instructions = format_instruction(instruction, 2)
        if self.get_param(instructions[0], inp[self.cursor + 1]) != 0:
            cursor_change = self.get_param(instructions[1], self.program[self.cursor + 2]) - self.cursor
        else:
            cursor_change = 3
        return cursor_change

    def execute_jump_if_false(self, instruction):
        instructions = format_instruction(instruction, 2)
        if self.get_param(instructions[0], self.program[self.cursor + 1]) == 0:
            cursor_change = self.get_param(instructions[1], self.program[self.cursor + 2]) - self.cursor
        else:
            cursor_change = 3
        return cursor_change

    def execute_less_than(self, instruction):
        instructions = format_instruction(instruction, 3)
        if self.get_param(instructions[0], self.program[self.cursor + 1]) < self.get_param(instructions[1], self.program[self.cursor + 2]):
            self.program[self.program[self.cursor + 3]] = 1
        else:
            self.program[self.program[self.cursor + 3]] = 0
        return 4

    def execute_equals(self, instruction):
        instructions = format_instruction(instruction, 3)
        if self.get_param(instructions[0], self.program[self.cursor + 1]) == self.get_param(instructions[1], inp[self.cursor + 2]):
            self.program[self.program[self.cursor + 3]] = 1
        else:
            self.program[self.program[self.cursor + 3]] = 0
        return 4


IntCode(inp, 5).run()
