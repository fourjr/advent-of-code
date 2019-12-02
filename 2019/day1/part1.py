with open('input.txt') as f:
    inp = f.read().splitlines()


def get_fuel(mass: int):
    # take its mass, divide by three, round down, and subtract 2.
    return mass // 3 - 2


sum_of_fuel = sum(get_fuel(int(m)) for m in inp)
print(sum_of_fuel)
