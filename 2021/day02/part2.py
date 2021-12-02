from aoc import get_input_as


inp = get_input_as()
x = 0
depth = 0
aim = 0

for line in inp:
    sp = line.split(' ')
    direction = sp[0]
    mag = int(sp[1])
    if direction == 'forward':
        x += mag
        depth += mag * aim
    if direction == 'down':
        aim += mag
    if direction == 'up':
        aim -= mag

print(x * depth)
