with open('input.txt') as f:
    inp = f.read()
wires = [i.split(',') for i in inp.splitlines()]

up_values = []
right_values = []
down_values = []
left_values = []
for w in wires:
    u = sum([int(x[1:]) for x in filter(lambda x: x.startswith('U'), w)])
    d = sum([int(x[1:]) for x in filter(lambda x: x.startswith('D'), w)])
    r = sum([int(x[1:]) for x in filter(lambda x: x.startswith('R'), w)])
    l = sum([int(x[1:]) for x in filter(lambda x: x.startswith('L'), w)])

    up_values.append(u)
    down_values.append(d)
    left_values.append(l)
    right_values.append(r)

rows = max(up_values) + max(down_values) + 3
columns = max(right_values) + max(left_values) + 3

print(rows, columns)

space = []
for i in range(rows):
    space.append(['.'] * columns)


def place_marker(wn):
    if space[cursor[0]][cursor[1]] in ('.', str(wn)):
        space[cursor[0]][cursor[1]] = str(wn)
    else:
        space[cursor[0]][cursor[1]] = 'X'


origin = [len(space) - max(down_values) - 2, 1 + max(left_values)]
cursor = origin[:]
space[cursor[0]][cursor[1]] = 'O'  # start
for wn, w in enumerate(wires):
    print('next')
    cursor = origin[:]
    for i in w:
        letter = i[0]
        location = int(i[1:])
        print(letter, location, cursor)
        if letter == 'U':
            for x in range(location):
                cursor[0] -= 1
                place_marker(wn)
        elif letter == 'D':
            for x in range(location):
                cursor[0] += 1
                place_marker(wn)
        elif letter == 'L':
            for x in range(location):
                cursor[1] -= 1
                place_marker(wn)
        elif letter == 'R':
            for x in range(location):
                cursor[1] += 1
                place_marker(wn)

# for i in space:
#     print(' '.join(i))

xs = []
for rn, row in enumerate(space):
    for cn, column in enumerate(row):
        if column == 'X':
            xs.append(sum((origin[0] - rn, cn - origin[1])))

print(min(xs))
