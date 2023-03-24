import aoc


inp = aoc.get_input_as()

tail_positions = set()
head = [0, 0]
knots = [[0, 0] for _ in range(9)]  # knots[8] is the tail
tail_positions.add(tuple(knots[8]))


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
        for n, knot in enumerate(knots):
            if n == 0:
                follow = head
            else:
                follow = knots[n - 1]

            horizontal_distance = follow[0] - knot[0]
            vertical_distance = follow[1] - knot[1]

            # no move criteria
            if horizontal_distance ** 2 + vertical_distance ** 2 <= 2:
                # directly beside or diagonal
                continue

            # move tail
            if abs(horizontal_distance) == 2 and vertical_distance == 0:
                knot[0] += aoc.sign(horizontal_distance)
            elif abs(vertical_distance) == 2 and horizontal_distance == 0:
                knot[1] += aoc.sign(vertical_distance)
            else:
                knot[0] += aoc.sign(horizontal_distance)
                knot[1] += aoc.sign(vertical_distance)

        tail_positions.add(tuple(knots[8]))

print(len(tail_positions))
