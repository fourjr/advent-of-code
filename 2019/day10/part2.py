import math
import operator
from collections import OrderedDict

class Tile:
    def __init__(self, coords, symbol):
        self.coords = coords
        self.symbol = symbol

    def can_see(self):
        see = {}
        x1, y1 = self.coords
        unpacked_map = [x for i in full_map for x in i]
        for i in unpacked_map:
            x2, y2 = i.coords
            if self == i or i.symbol != '#':
                continue

            angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
            dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            if angle < 0:
                angle = 360 - abs(angle)
            angle -= 270
            if angle < 0:
                angle = 360 - abs(angle)

            if angle in see:
                if see[angle][1] > dist:
                    see[angle] = (i, dist)
            else:
                see[angle] = (i, dist)

        return {k: v[0] for k, v in see.items()}

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.coords == other.coords
        
        if isinstance(other, tuple):
            return self.coords == other

        return super().__eq__(other)

    def __repr__(self):
        return f'<Tile coords={self.coords} symbol={self.symbol}>'


with open('input.txt') as f:
    full_map = [[Tile((c, r), x) for c, x in enumerate(l)] for r, l in enumerate(f.read().splitlines())]

sighted = {}
station_position = None
for r in full_map:
    for c in r:
        if c.symbol == '#':
            cs = c.can_see()
            if len(sighted) < len(cs):
                sighted = cs
                station_position = c.coords

s_sorted = OrderedDict(sorted(sighted.items(), key=operator.itemgetter(0)))
s_sorted_keys = iter(list(s_sorted.keys()))
for _ in range(200):
    try:
        k = next(s_sorted_keys)
    except StopIteration:
        sighted = full_map[station_position[1]][station_position[0]].can_see()
        s_sorted = OrderedDict(sorted(sighted.items(), key=operator.itemgetter(0)))
        s_sorted_keys = iter(list(s_sorted.keys()))
        k = next(s_sorted_keys)

    full_map[s_sorted[k].coords[1]][s_sorted[k].coords[0]].symbol = '.'
    last_removed = s_sorted.pop(k)

coords = last_removed.coords
print(coords[0] * 100 + coords[1])
