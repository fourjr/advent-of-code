from enum import IntEnum

# with open('input.txt') as f:
inp = '3,225,1,225,6,6,1100,1,238,225,104,0,1102,31,68,225,1001,13,87,224,1001,224,-118,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1,174,110,224,1001,224,-46,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,13,60,224,101,-73,224,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1101,87,72,225,101,47,84,224,101,-119,224,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,1101,76,31,225,1102,60,43,225,1102,45,31,225,1102,63,9,225,2,170,122,224,1001,224,-486,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,29,17,224,101,-493,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,1102,52,54,225,1102,27,15,225,102,26,113,224,1001,224,-1560,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1002,117,81,224,101,-3645,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1108,677,226,224,102,2,223,223,1006,224,344,101,1,223,223,108,677,226,224,102,2,223,223,1006,224,359,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,374,101,1,223,223,1007,226,677,224,102,2,223,223,1005,224,389,101,1,223,223,8,677,677,224,102,2,223,223,1006,224,404,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,419,101,1,223,223,1108,677,677,224,1002,223,2,223,1005,224,434,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,449,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,464,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,7,677,677,224,102,2,223,223,1006,224,494,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,509,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,524,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,539,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,554,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,569,101,1,223,223,1008,226,677,224,102,2,223,223,1005,224,584,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,599,101,1,223,223,1007,226,226,224,1002,223,2,223,1005,224,614,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,629,101,1,223,223,107,677,226,224,1002,223,2,223,1005,224,644,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,674,1001,223,1,223,4,223,99,226'
inp = [int(x) for x in inp.split(',')]
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
