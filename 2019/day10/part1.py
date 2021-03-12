import math

class Tile:
    def __init__(self, coords, symbol):
        self.coords = coords
        self.symbol = symbol

    def can_see(self):
        see = set()
        x1, y1 = self.coords
        unpacked_map = [x for i in full_map for x in i]
        for i in unpacked_map:
            x2, y2 = i.coords
            if self == i or i.symbol != '#':
                continue

            angle = math.atan2(y2 - y1, x2 - x1)
            see.add(angle)

        return len(see)

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.coords == other.coords

        return super().__eq__(other)

    def __repr__(self):
        return f'<Tile coords={self.coords} symbol={self.symbol}>'


with open('input.txt') as f:
    full_map = [[Tile((c, r), x) for c, x in enumerate(l)] for r, l in enumerate(f.read().splitlines())]

max_val = 0
for r in full_map:
    for c in r:
        if c.symbol == '#':
            cs = c.can_see()
            if max_val < cs:
                max_val = cs

print(max_val)
