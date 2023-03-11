import re

import aoc


counter = 0
scanner = [None] * 14
code = aoc.get_input_as()[0]

for num, char in enumerate(code):
    cursor = num % 14
    scanner[cursor] = char
    if all(x is not None for x in scanner) and len(set(scanner)) == 14:
        print(num + 1)
        break