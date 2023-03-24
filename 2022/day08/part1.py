import aoc


grid = []
inp = aoc.get_input_as()
for line in inp:
    grid.append(list(map(int, line)))

rows = len(grid)
columns = len(grid[0])

scenic_scores = set()

for r in range(rows):
    for c in range(columns):
        elem = grid[r][c]
        score = 1

        for r_offset, c_offset in ((0, -1), (0, +1), (-1, 0), (+1, 0)):
            r_cursor = r + r_offset
            c_cursor = c + c_offset
            num_trees = 0

            while c_cursor >= 0 and c_cursor < columns and r_cursor >= 0 and r_cursor < rows:
                num_trees += 1

                if grid[r_cursor][c_cursor] >= elem:
                    # blocked
                    break
                r_cursor += r_offset
                c_cursor += c_offset

            if num_trees != 0:
                score *= num_trees
        scenic_scores.add(score)

print(max(scenic_scores))
