import aoc


inp = aoc.get_input_as()
full_map = []
for y, line in enumerate(inp):
    if 'S' in line:
        start = (line.index('S'), y)
    full_map.append(list(line))

x_size = len(full_map[0])
y_size = len(full_map)

def path(point, count=0, from_point=None):
    x, y = point
    print(point)
    if full_map[y][x] == 'E':
        return count
    exc = []
    # if x - 1 > 0 and (ord(full_map[y][x-1]) - ord(full_map[y][x]) <= 1 or full_map[y][x] == 'S') and from_point != (y, x-1):
    #     exc.append((y, x-1))
    # if x + 1 < x_size and (ord(full_map[y][x+1]) - ord(full_map[y][x]) <= 1 or full_map[y][x] == 'S') and from_point != (y, x+1):
    #     exc.append((y, x+1))
    # if y - 1 > 0 and (ord(full_map[y-1][x]) - ord(full_map[y][x]) <= 1 or full_map[y][x] == 'S') and from_point != (y-1, x):
    #     exc.append((y-1, x))
    if y + 1 < y_size and (ord(full_map[y+1][x]) - ord(full_map[y][x]) <= 1 or full_map[y][x] == 'S') and from_point != (y+1, x):
        exc.append((y+1, x))
    if len(exc) == 0:
        return None
    vals = []
    for i in exc:
        vals.append(path(i, count+1, point))
    return min(vals for x in vals if x is not None)

path(start, 0)
