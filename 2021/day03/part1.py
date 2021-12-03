from collections import Counter
from aoc import get_input_as

inp = get_input_as(str)
bit_count = len(inp[0])
gamma = ''
epsilon = ''

for i in range(bit_count):
    counter = Counter([x[i] for x in inp])
    gamma += counter.most_common(1)[0][0]
    epsilon += counter.most_common()[-1][0]

print(int(gamma, 2) * int(epsilon, 2))
