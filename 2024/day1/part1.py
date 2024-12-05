import aoc


vals = aoc.get_input_as(sep='\n')
all_left = []
all_right = []
for (left, right) in [map(int, i.split('   ')) for i in vals]:
    all_left.append(left)
    all_right.append(right)

sorted_left = sorted(all_left)
sorted_right = list(sorted(all_right))

total = 0
for n, i in enumerate(sorted_left):
    total += abs(sorted_right[n] - i)

print(total)
