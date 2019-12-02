import copy

with open('input.txt') as f:
    original_inp = [int(x) for x in f.read().split(',')]

# replace position 1 with the value 12 and replace position 2 with the value 2
target = 19690720
noun = 0
verb = 0

while True:
    inp = copy.deepcopy(original_inp)
    inp[1] = noun
    inp[2] = verb
    cursor = 0

    while inp[cursor] != 99:
        if inp[cursor] == 1:
            # Add
            inp[inp[cursor + 3]] = inp[inp[cursor + 1]] + inp[inp[cursor + 2]]
        elif inp[cursor] == 2:
            # Multiply
            inp[inp[cursor + 3]] = inp[inp[cursor + 1]] * inp[inp[cursor + 2]]

        cursor += 4

    if inp[0] != target:
        verb += 1
        if verb == 100:
            noun += 1
            verb = 0
            if noun == 100:
                break
    else:
        print(100 * noun + verb)
        break
