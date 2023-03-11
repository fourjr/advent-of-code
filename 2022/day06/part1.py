import re

import aoc


counter = 0
scanner = [None] * 4
code = aoc.get_input_as()[0]

for num, char in enumerate(code):
    cursor = num % 4
    scanner[cursor] = char
    if all(x is not None for x in scanner) and len(set(scanner)) == 4:
        print(num + 1)
        break