import aoc


total_count = 0

grid = []
inp = aoc.get_input_as()
for line in inp:
    grid.append(list(map(int, line)))

rows = len(grid)
columns = len(grid[0])

for r in range(rows):
    for c in range(columns):
        elem = grid[r][c]

        for r_offset, c_offset in ((0, -1), (0, +1), (-1, 0), (+1, 0)):
            r_cursor = r + r_offset
            c_cursor = c + c_offset
            can_see = True

            while c_cursor >= 0 and c_cursor < columns and r_cursor >= 0 and r_cursor < rows:
                if grid[r_cursor][c_cursor] >= elem:
                    # cant see
                    can_see = False
                    break
                c_cursor += c_offset
                r_cursor += r_offset

            if can_see:
                total_count += 1
                break


print(total_count)