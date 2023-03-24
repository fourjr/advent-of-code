import aoc


inp = aoc.get_input_as()

tail_positions = set()
head = [0, 0]
tail = [0, 0]
tail_positions.add(tuple(tail))


for line in inp:
    direction, steps = line.split(' ')
    steps = int(steps)
    for i in range(steps):
        if direction == 'D':
            head[1] -= 1
        if direction == 'U':
            head[1] += 1
        if direction == 'L':
            head[0] -= 1
        if direction == 'R':
            head[0] += 1

        # move tail
        horizontal_distance = head[0] - tail[0]
        vertical_distance = head[1] - tail[1]

        # no move criteria
        if horizontal_distance ** 2 + vertical_distance ** 2 <= 2:
            # directly beside or diagonal
            continue

        # move tail
        if abs(horizontal_distance) == 2 and vertical_distance == 0:
            tail[0] += aoc.sign(horizontal_distance)
        elif abs(vertical_distance) == 2 and horizontal_distance == 0:
            tail[1] += aoc.sign(vertical_distance)
        else:
            tail[0] += aoc.sign(horizontal_distance)
            tail[1] += aoc.sign(vertical_distance)

        tail_positions.add(tuple(tail))

print(len(tail_positions))
