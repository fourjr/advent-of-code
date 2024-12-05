import re

import aoc


program = aoc.get_input(sep=-1)
valid_commands = re.findall(r'(mul\(\d+,\d+\))|(do\(\))|(don\'t\(\))', program)

accepting_mul = True
total = 0
for cmd in valid_commands:
    if cmd[1] == 'do()':
        accepting_mul = True
    elif cmd[2] == "don't()":
        accepting_mul = False
    else:
        match = re.match(r'mul\((\d+),(\d+)\)', cmd[0])
        m1 = match.group(1)
        m2 = match.group(2)
        if accepting_mul:
            total += int(m1) * int(m2)

print(total)
