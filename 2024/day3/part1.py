import re

import aoc


program = aoc.get_input(sep=-1)
matches = re.findall(r'mul\((\d+),(\d+)\)', program)

total = 0
for m1, m2 in matches:
    total += int(m1) * int(m2)

print(total)
