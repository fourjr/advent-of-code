from enum import IntEnum

with open('input.txt') as f:
    inp = [int(x) for x in f.read().split(',')]
cursor = 0


class Mode(IntEnum):
    POSITION = 0
    IMMEDIATE = 1


def format_instruction(instruction, length):
    instruction = str(instruction)
    while len(instruction) < length:
        instruction = '0' + instruction

    return [Mode(int(x)) for x in reversed(instruction)]


def get_param(mode, value):
    if mode == Mode.POSITION:
        return inp[value]
    elif mode == Mode.IMMEDIATE:
        return value


def add(instruction):
    instructions = format_instruction(instruction, 3)
    inp[inp[cursor + 3]] = get_param(instructions[0], inp[cursor + 1]) + get_param(instructions[1], inp[cursor + 2])

    return 4


def multiply(instruction):
    instructions = format_instruction(instruction, 3)
    inp[inp[cursor + 3]] = get_param(instructions[0], inp[cursor + 1]) * get_param(instructions[1], inp[cursor + 2])

    return 4


def input_save(instruction):
    inputval = 1
    inp[inp[cursor + 1]] = inputval

    return 2


def output_stdout(instruction):
    instructions = format_instruction(instruction, 1)
    print(cursor, get_param(instructions[0], inp[cursor + 1]))

    return 2


def jump_if_true(instruction):
    instructions = format_instruction(instruction, 2)
    if get_param(instructions[0], inp[cursor + 1]) != 0:
        cursor_change = get_param(instructions[1], inp[cursor + 2]) - cursor
    else:
        cursor_change = 3
    return cursor_change


def jump_if_false(instruction):
    instructions = format_instruction(instruction, 2)
    if get_param(instructions[0], inp[cursor + 1]) == 0:
        cursor_change = get_param(instructions[1], inp[cursor + 2]) - cursor
    else:
        cursor_change = 3
    return cursor_change


def less_than(instruction):
    instructions = format_instruction(instruction, 3)
    if get_param(instructions[0], inp[cursor + 1]) < get_param(instructions[1], inp[cursor + 2]):
        inp[inp[cursor + 3]] = 1
    else:
        inp[inp[cursor + 3]] = 0
    return 4


def equals(instruction):
    instructions = format_instruction(instruction, 3)
    if get_param(instructions[0], inp[cursor + 1]) == get_param(instructions[1], inp[cursor + 2]):
        inp[inp[cursor + 3]] = 1
    else:
        inp[inp[cursor + 3]] = 0
    return 4


while int(str(inp[cursor])[-2:]) != 99:
    no_of_params = 0
    opcode = int(str(inp[cursor])[-2:])
    if opcode == 1:
        # Add
        no_of_params = add(str(inp[cursor])[:-2])
    elif opcode == 2:
        # Multiply
        no_of_params = multiply(str(inp[cursor])[:-2])
    elif opcode == 3:
        # Input
        no_of_params = input_save(str(inp[cursor])[:-2])
    elif opcode == 4:
        # Output
        no_of_params = output_stdout(str(inp[cursor])[:-2])
    elif opcode == 5:
        # Jump if true
        no_of_params = jump_if_true(str(inp[cursor])[:-2])
    elif opcode == 6:
        # Jump if false
        no_of_params = jump_if_false(str(inp[cursor])[:-2])
    elif opcode == 7:
        # Less than
        no_of_params = less_than(str(inp[cursor])[:-2])
    elif opcode == 8:
        # Equals
        no_of_params = equals(str(inp[cursor])[:-2])

    cursor += no_of_params
