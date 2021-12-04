from aoc import get_input_as


class Board:
    def __init__(self, data):
        self.rows = []
        self.running = True
        spl = data.splitlines()
        for x in spl:
            row = []
            while x:
                row.append([int(x[:2].strip()), False])
                x = x[2:].strip()
            self.rows.append(row)

    def play_num(self, num):
        if not self.running:
            return
        for nr, r in enumerate(self.rows):
            for nc, (c, _) in enumerate(r):
                if c == num:
                    self.rows[nr][nc][1] = True
                    break

    def check_win(self):
        if not self.running:
            return False

        for r in self.rows:
            if all(x[1] for x in r):
                return True

        for c in range(len(self.rows)):
            col = []
            for r in self.rows:
                col.append(r[c])
            if all(c[1] for c in col):
                return True
        return False

    def get_score(self, num):
        unmarked_sum = 0
        for r in self.rows:
            for c, checked in r:
                if not checked:
                    unmarked_sum += c
        return unmarked_sum * num


inp = get_input_as(str, sep='\n\n')

draw = map(int, inp.pop(0).split(','))
boards = []
for i in inp:
    boards.append(Board(i))

for num in draw:
    for board in boards:
        board.play_num(num)
        if board.check_win():
            print(board.get_score(num))
            exit(0)
