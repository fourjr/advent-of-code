from collections import Counter

import aoc

vals = aoc.get_input_as(callback=lambda x: map(int, x.split(' ')), sep='\n')

    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.

all_left = []
all_right = []
for (left, right) in [map(int, i.split('   ')) for i in vals]:
    all_left.append(left)
    all_right.append(right)

sorted_right = Counter(all_right)

total = 0
for i in all_left:
    total += i * sorted_right[i]

print(total)
