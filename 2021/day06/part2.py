from collections import defaultdict
from aoc import get_input_as, submit


inp = get_input_as(int, sep=',')

lanternfish = defaultdict(int)
triggers = defaultdict(list)

for i in inp:
    lanternfish[i + 1] += 1
counter = len(inp)

for i in range(1, 256 + 1):
    if i in lanternfish:
        counter += lanternfish[i]
        lanternfish[i + 7] += lanternfish[i]
        lanternfish[i + 9] += lanternfish[i]
        del lanternfish[i]

submit(counter)
