from typing import Union


class GameList(list):
    def __getitem__(self, item):
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start and start >= len(self):
                start %= len(self)

            if stop and stop >= len(self):
                stop %= len(self)
                if stop > start:
                    return super().__getitem__(slice(start, stop, item.step))
                else:
                    return super().__getitem__(slice(start, len(self), item.step)) + super().__getitem__(slice(0, stop, item.step))

            return super().__getitem__(slice(start, stop, item.step))

        elif isinstance(item, int):
            if item >= len(self):
                return super().__getitem__(item % len(self))

        return super().__getitem__(item)

    def __delitem__(self, item: Union[int, slice]) -> None:
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start >= len(self):
                start %= len(self)

            if stop >= len(self):
                stop %= len(self)
                if stop > start:
                    return super().__delitem__(slice(start, stop, item.step))
                else:
                    return super().__delitem__(slice(start, len(self), item.step)) + super().__delitem__(slice(0, stop, item.step))

            return super().__delitem__(slice(start, stop, item.step))

        elif isinstance(item, int):
            if item >= len(self):
                return super().__delitem__(item % len(self))

        return super().__delitem__(item)

input_val = 853192647
game = GameList(map(int, str(input_val)))

for i in range(max(game) + 1, 1000000 + 1):
    game.append(i)

cursor = 0
for i in range(10000000):
    cursor_val = game[cursor]
    pick_up = game[cursor + 1:cursor + 4]
    dest = game[cursor] - 1
    if dest < min(game):
        dest = max(game)
    while dest in pick_up:
        dest -= 1
        if dest < min(game):
            dest = max(game)

    v1 = game[cursor + 1]
    v2 = game[cursor + 2]
    v3 = game[cursor + 3]

    del game[cursor + 1]
    cursor = game.index(cursor_val)
    del game[cursor + 1]
    cursor = game.index(cursor_val)
    del game[cursor + 1]

    dest = game.index(dest)
    game.insert(dest + 1, v3)
    game.insert(dest + 1, v2)
    game.insert(dest + 1, v1)
    
    cursor = game.index(cursor_val) + 1

one_index = game.index(1)
print(game[one_index + 1] * game[one_index + 2])