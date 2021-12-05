import math
from aoc import get_input_as, submit


inp = get_input_as(str)

lines = set()
overlaps = set()

for line in inp:
    c1, c2 = line.split(' -> ')
    x1, y1 = map(int, c1.split(','))
    x2, y2 = map(int, c2.split(','))
    if x1 == x2:
        yf = min((y1, y2))
        yl = max((y1, y2))
        for y in range(yf, yl + 1):
            if (x1, y) in lines:
                overlaps.add((x1, y))
            lines.add((x1, y))
    elif y1 == y2:
        xf = min((x1, x2))
        xl = max((x1, x2))
        for x in range(xf, xl + 1):
            if (x, y1) in lines:
                overlaps.add((x, y1))
            lines.add((x, y1))
    else:
        dist = abs(x1 - x2) + 1

        currx = x1
        curry = y1
        xmag = int(math.copysign(1, x2 - x1))
        ymag = int(math.copysign(1, y2 - y1))
        for i in range(dist):
            if (currx, curry) in lines:
                overlaps.add((currx, curry))
            lines.add((currx, curry))
            currx += xmag
            curry += ymag

submit(len(overlaps))
