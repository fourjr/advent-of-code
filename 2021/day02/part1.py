from aoc import get_input_as


inp = get_input_as()
x = 0
depth = 0

for line in inp:
    sp = line.split(' ')
    direction = sp[0]
    mag = int(sp[1])
    if direction == 'forward':
        x += mag
    if direction == 'down':
        depth += mag
    if direction == 'up':
        depth -= mag

print(x * depth)
