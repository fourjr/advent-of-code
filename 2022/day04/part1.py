import aoc


count = 0

for p1, p2 in aoc.get_input_as(lambda x: [set(range(int(i.split('-')[0]), int(i.split('-')[1]) + 1)) for i in x.split(',')]):
    if len(p1.intersection(p2)) == len(p1) or len(p2.intersection(p1)) == len(p2):
        count += 1

print(count)