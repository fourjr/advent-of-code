import string

import aoc


mapping = string.ascii_letters

count = 0

for c1, c2 in aoc.get_input_as(lambda x: (set(x[len(x) // 2:]), set(x[:len(x) // 2]))):
    for i in c1.intersection(c2):
        count += mapping.find(i) + 1

print(count)