with open('input.txt') as f:
    inp = list(map(int, f.read().splitlines()))

count = 0

for n, val in enumerate(inp[:-3]):
    # if val > inp[n - 1]:
    window = val + inp[n + 1] + inp[n + 2]
    next_window = inp[n + 1] + inp[n + 2] + inp[n + 3]
    if next_window > window:
        count += 1

print(count)
