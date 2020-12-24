from collections import defaultdict

with open('input.txt') as f:
    tiles = f.readlines()

# WHITE: True
# BLACK: False

tilemap = defaultdict(lambda: defaultdict(lambda: True))
possible_directions = ['e', 'se', 'sw', 'w', 'nw', 'ne']

for t in tiles:
    instructions = []
    cursor = 0

    x = 0
    y = 0

    while cursor < len(t):
        if t[cursor] in possible_directions:
            instructions.append(t[cursor])
            cursor += 1
        else:
            instructions.append(t[cursor:cursor + 2])
            cursor += 2

    for ins in instructions:
        # print(ins)
        if ins == 'e':
            x += 1
        if ins == 'w':
            x -= 1

        if y % 2 == 0:
            if ins == 'ne':
                y -= 1
            if ins == 'nw':
                x -= 1
                y -= 1
            if ins == 'se':
                y += 1
            if ins == 'sw':
                x -= 1
                y += 1
        else:
            if ins == 'ne':
                x += 1
                y -= 1
            if ins == 'nw':
                y -= 1
            if ins == 'se':
                x += 1
                y += 1
            if ins == 'sw':
                y += 1

    tilemap[x][y] = not tilemap[x][y]

count = 0
for x, row in tilemap.items():
    for y, tile in row.items():
        if not tile:
            count += 1

print(count)
