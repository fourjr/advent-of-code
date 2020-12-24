import copy

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


def get_color(val):
    return tilemap_lookup[val[0]][val[1]]

for _ in range(100):
    # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
    # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
    min_x = min(x for x in tilemap.keys())
    max_x = max(x for x in tilemap.keys())

    min_y = min(y for x in tilemap.values() for y in x.keys())
    max_y = max(y for x in tilemap.values() for y in x.keys())

    for e in range(min_x - 1, max_x + 2):
        if e not in tilemap:
            tilemap[e][0] = True

    for x in tilemap.keys():
        for e in range(min_y - 1, max_y + 2):
            if e not in tilemap[x]:
                tilemap[x][e] = True

    tilemap_lookup = copy.deepcopy(tilemap)
    flip = []
    for x, row in tilemap.items():
        for y, tile in row.items():
            if y % 2 == 0:
                adjacents = [
                    (x + 1, y + 0),
                    (x + 0, y - 1),
                    (x - 1, y - 1),
                    (x - 1, y + 0),
                    (x - 1, y + 1),
                    (x + 0, y + 1),
                ]
            else:
                adjacents = [
                    (x + 1, y + 0),
                    (x + 1, y - 1),
                    (x + 0, y - 1),
                    (x - 1, y + 0),
                    (x + 0, y + 1),
                    (x + 1, y + 1),
                ]
            adjacents = map(get_color, adjacents)
            black_count = len([i for i in adjacents if not i])
            if tile:
                if black_count == 2:
                    tilemap[x][y] = not tilemap[x][y]
            else:
                if black_count == 0 or black_count > 2:
                    tilemap[x][y] = not tilemap[x][y]

count = 0
for x, row in tilemap.items():
    for y, tile in row.items():
        if not tile:
            count += 1

print(count)
