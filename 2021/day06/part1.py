from aoc import get_input_as, submit

inp = get_input_as(int, sep=',')


class Lanternfish:
    def __init__(self, age):
        self.age = age

    def pass_day(self):
        self.age -= 1
        if self.age < 0:
            self.age = 6
            newfish = Lanternfish(8)
            return [newfish]
        return []

    def __repr__(self) -> str:
        return str(self.age)


fishes = list(map(Lanternfish, inp))

for i in range(80):
    for f in list(fishes):
        fishes.extend(f.pass_day())

answer = len(fishes)
submit(answer)
