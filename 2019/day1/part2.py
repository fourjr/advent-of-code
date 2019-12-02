with open('input.txt') as f:
    inp = f.read().splitlines()


def get_fuel(mass: int):
    # take its mass, divide by three, round down, and subtract 2.
    fuel = mass // 3 - 2
    if fuel < 0:
        return 0

    return fuel + get_fuel(fuel)


sum_of_fuel = sum(get_fuel(int(m)) for m in inp)
print(sum_of_fuel)
