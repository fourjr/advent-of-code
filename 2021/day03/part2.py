from collections import Counter
from aoc import get_input_as

inp = get_input_as(str)
bit_count = len(inp[0])

candidates = list(inp)
for bit_index in range(bit_count):
    counter = Counter([x[bit_index] for x in candidates])
    # o2 gen
    most_common_bit = counter.most_common()[0][0]
    if counter.most_common()[0][1] == counter.most_common()[1][1]:
        most_common_bit = '1'

    old_candidates = list(candidates)
    candidates = []
    for val in old_candidates:
        if val[bit_index] == most_common_bit:
            candidates.append(val)

    if len(candidates) == 1:
        o2_gen = int(candidates[0], 2)
        break

candidates = list(inp)
for bit_index in range(bit_count):
    # co2 scrubber
    counter = Counter([x[bit_index] for x in candidates])
    least_common_bit = counter.most_common()[-1][0]
    if counter.most_common()[0][1] == counter.most_common()[-1][1]:
        least_common_bit = '0'

    old_candidates = list(candidates)
    candidates = []
    for val in old_candidates:
        if val[bit_index] == least_common_bit:
            candidates.append(val)

    if len(candidates) == 1:
        co2_scrub = int(candidates[0], 2)
        break

print(o2_gen * co2_scrub)
