import string

import aoc


mapping = string.ascii_letters

count = 0

groups = []
for num, line in enumerate(aoc.get_input_as(set)):
    if num % 3 == 0:
        groups.append([])
    groups[-1].append(line)

for c1, c2, c3 in groups:
    badge = c1.intersection(c2).intersection(c3)
    assert len(badge) == 1
    count += mapping.find(next(iter(badge))) + 1

print(count)