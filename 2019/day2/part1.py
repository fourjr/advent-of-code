with open('input.txt') as f:
    inp = [int(x) for x in f.read().split(',')]

# replace position 1 with the value 12 and replace position 2 with the value 2
inp[1] = 12
inp[2] = 2
cursor = 0

while inp[cursor] != 99:
    if inp[cursor] == 1:
        # Add
        inp[inp[cursor + 3]] = inp[inp[cursor + 1]] + inp[inp[cursor + 2]]
    elif inp[cursor] == 2:
        # Multiply
        inp[inp[cursor + 3]] = inp[inp[cursor + 1]] * inp[inp[cursor + 2]]

    cursor += 4

print(inp[0])
