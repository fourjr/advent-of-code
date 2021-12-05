import copy
import math
from collections import defaultdict
from enum import Enum
from typing import DefaultDict, Iterable, List, Set

import numpy as np

from aoc import get_input_as, submit


inp = get_input_as(str, sep='\n\n')


class FlipVariant(Enum):
    ORIGINAL   = 0b0000
    VERTICAL   = 0b0100
    HORIZONTAL = 0b1000


class RotateVariant(Enum):
    ORIGINAL   = 0b0000
    D090       = 0b0001
    D180       = 0b0010
    D270       = 0b0011


class TileVariant:
    def __init__(self, variant, data, tile):
        self.variant = variant
        self.pixels: List[List[str]] = data
        self.tile = tile
        self.id = f'{tile.id}.{variant}'

        self.top_edge = ''.join(self.pixels[0])
        self.bottom_edge = ''.join(self.pixels[len(self.pixels) - 1])
        self.left_edge = ''.join(self.pixels.transpose()[0])
        self.right_edge = ''.join(self.pixels.transpose()[-1])

    def rotate90(self, k=1):
        flip_bits = self.variant >> 2
        rotate_bits = 0b0011 & self.variant
        rotate_bits += 1
        variant = (flip_bits << 2) | rotate_bits
        return TileVariant(variant, np.rot90(self.pixels, k), self.tile)

    def __repr__(self) -> str:
        return f'<TileVariant id={self.id} variant={bin(self.variant)} tile={self.tile.id}>'

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, TileVariant):
            return self.id == o.id
        return super().__eq__(o)


class Tile:
    def __init__(self, data):
        """data: str"""
        self.state = None
        self.original = None
        self.next = None
        self.prev = None

        data = data.splitlines()
        header = data.pop(0)
        self.id = int(header[5:-1])
        self.pixels = np.array([list(x) for x in data])
        self.size = len(self.pixels[0])

        self.variants = {}
        for flip_v in FlipVariant:
            var = self.flip(flip_v)
            for rotate_v in RotateVariant:
                if rotate_v != RotateVariant.ORIGINAL:
                    var = var.rotate90()
                self.variants[var.variant] = var

    def flip(self, variant):
        if variant == FlipVariant.VERTICAL:
            new_data = np.flipud(self.pixels)
        elif variant == FlipVariant.HORIZONTAL:
            new_data = np.fliplr(self.pixels)
        else:
            new_data = self.pixels

        return TileVariant(variant.value, new_data, self)

    def __repr__(self) -> str:
        return f'<Tile id={self.id} pixels={len(self.pixels)}>'

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Tile):
            return self.id == o.id
        return super().__eq__(o)

    def __hash__(self) -> int:
        return hash(self.id)


class CameraArray:
    def __init__(self, data) -> None:
        self.head = None
        self.tail = None

        self.tiles = []
        prev = None
        for i in data:
            tile = Tile(i)
            self.tiles.append(tile)
            tile.prev = prev

            if prev is not None:
                prev.next = tile

            prev = tile

        self.head = self.tiles[0]
        self.tail = self.tiles[-1]

        self.size = int(math.sqrt(len(self.tiles)))
        self.all_variants: Set[TileVariant] = {x for t in self.tiles for x in t.variants.values()}

    def coherence_check(self) -> bool:
        tiles = list(self)
        for index, tile in enumerate(tiles):
            check_top = index - 10
            check_left = index - 1
            if index % self.size == 0:
                # extreme left
                check_left = None
                pass
            if check_top < 0:
                # top row
                check_top = None

            # Checking
            conditions = (
                check_left is None or tile.left_edge == self.tiles[check_left].right_edge,
                check_top is None or tile.top_edge == self.tiles[check_top].top_edge,
            )

            if not all(conditions):
                return False

        return True

    def __iter__(self) -> Iterable[Tile]:
        curr = self.head
        yield curr

        while curr.next:
            curr = curr.next
            if curr is self.tail:
                yield curr
                return

            yield curr

    def get_top_left_candidates(self):
        right_cands: DefaultDict[List[TileVariant]] = defaultdict(list)
        for v1 in self.all_variants:
            for v2 in self.all_variants:
                # Check for right edge match
                if v1.tile != v2.tile:
                    if v1.right_edge == v2.left_edge:
                        right_cands[v1].append(v2)

        maps = []
        tiles = []
        confirmed = [False] * len(self.tiles)
        confirmed[0] = True
        confirmed[1] = True
        confirmed[self.size] = True
        for t in self.tiles:
            tiles.append(t.variants[0b0])

        for v1 in right_cands.keys():
            tiles[0] = v1

            for v2 in self.all_variants:
                if v1.bottom_edge == v2.top_edge and v2.tile != v1.tile:
                    tiles[self.size] = v2
                    for r in right_cands[v1]:
                        if r.tile != v2.tile:
                            tiles[1] = r
                            maps.append(MapVariant(tiles, confirmed, self, 0))

        return maps

    def get_answer(self):
        left_candidates = self.get_top_left_candidates()
        answers = {x.short_id for x in self.call_get_next(left_candidates)}
        assert len(answers) == 1
        return list(answers)[0]

    def call_get_next(self, possibilites):
        if not possibilites:
            raise StopIteration

        all_possibilities = set()
        for i in possibilites:
            all_possibilities |= i.find_next()

        if len(all_possibilities) == 1:
            return all_possibilities

        try:
            return self.call_get_next(all_possibilities)
        except StopIteration:
            return all_possibilities


class MapVariant:
    def __init__(self, new_map: List[TileVariant], confirmed: List[bool], original: CameraArray, curr_index: int):
        self.map = copy.copy(new_map)
        self.confirmed = confirmed[:]
        self.curr_index = curr_index
        self.original = original
        self.size = original.size

        ids = []
        for n, i in enumerate(self.map):
            if self.confirmed[n]:
                ids.append(i.id)
            else:
                ids.append('')

        self.id = '-'.join(ids)
        self.short_id = self.map[0].tile.id * self.map[self.size - 1].tile.id * self.map[self.size * (self.size - 1)].tile.id * self.map[-1].tile.id

    @property
    def used_tiles(self) -> List[Tile]:
        used_tiles = set()
        for n, i in enumerate(self.confirmed):
            if i:
                used_tiles.add(self.map[n].tile)

        return used_tiles

    def find_next(self):
        self.curr_index += 1
        if self.curr_index >= len(self.map):
            raise StopIteration

        index = self.curr_index
        curr = self.map[self.curr_index]

        check_bottom = index + self.size
        check_right = index + 1

        # special cases
        if (index + 1) % self.size != 0 and self.confirmed[check_right]:
            # force a check right
            if curr.right_edge != self.map[check_right].left_edge:
                return []

        if check_bottom < len(self.map) and self.confirmed[check_bottom]:
            if curr.bottom_edge != self.map[check_bottom].top_edge:
                return []

        # back to normal
        if (index + 1) % self.size == 0 or self.confirmed[check_right]:
            # extreme right
            check_right = None

        if check_bottom >= len(self.map) or self.confirmed[check_bottom]:
            # top row
            check_bottom = None

        right_cands = []
        if check_right:
            for v in self.original.all_variants:
                if curr.right_edge == v.left_edge and v.tile not in self.used_tiles:
                    right_cands.append(v)

        newmaps = set()

        if check_bottom:
            for v in self.original.all_variants:
                if v.tile in self.used_tiles:
                    continue

                if check_right:
                    self.confirmed[check_right] = True
                    for r in right_cands:
                        self.map[check_right] = r
                        if curr.bottom_edge == v.top_edge and r.tile != v.tile:
                            self.confirmed[check_bottom] = True
                            self.map[check_bottom] = v

                            newmaps.add(MapVariant(self.map, self.confirmed, self.original, self.curr_index))
                    self.confirmed[check_right] = False
                else:
                    if curr.bottom_edge == v.top_edge:
                        self.confirmed[check_bottom] = True
                        self.map[check_bottom] = v
                        newmaps.add(MapVariant(self.map, self.confirmed, self.original, self.curr_index))

        else:
            for r in right_cands:
                self.confirmed[check_right] = True
                self.map[check_right] = r
                newmaps.add(MapVariant(self.map, self.confirmed, self.original, self.curr_index))

        if not any((check_bottom, check_right)):
            newmaps.add(self)

        return newmaps

    def __hash__(self) -> int:
        return self.short_id

    def __eq__(self, o: object) -> bool:
        if isinstance(o, MapVariant):
            return self.short_id == o.short_id
        return super().__eq__(o)

    def __repr__(self) -> str:
        return f'<MapVariant id={self.id} short_id={self.short_id}>'

    def __str__(self):
        size = self.size
        fmt = ''
        rows = len(self.map[0].pixels)

        for tr in range(size):
            for r in range(rows):
                for m in range(size):
                    fmt += ''.join(self.map[tr * size + m].pixels[r]) + ' '
                fmt += '\n'
            fmt += '\n'

        return fmt.strip()


cam = CameraArray(inp)
answer = cam.get_answer()
submit(answer)
