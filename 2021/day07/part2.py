from collections import Counter

from aoc import get_input_as, submit


inp = get_input_as(int, sep=',')
vals = Counter()

for i in inp:
    vals[i] += 1

maxval = max(inp)

most_common = vals.most_common()
weight = Counter()
for nn, (val, count) in enumerate(most_common):
    for i in range(maxval):
        n = abs(val - i)
        sumn = int(n * (n + 1) / 2)
        weight[i] += sumn * count


submit(weight.most_common()[-1][1])
