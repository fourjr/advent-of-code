import aoc
import numpy as np


rows = aoc.get_input(sep='\n')
grid = np.array([list(row) for row in rows])
xmas_count = 0
new_grid = np.zeros(grid.shape, dtype=str)
new_grid.fill('.')
for r, c in np.argwhere(grid == 'A'):
    conditions = []
    if r - 1 >= 0 and r + 1 < grid.shape[0] and c - 1 >= 0 and c + 1 < grid.shape[1]:
        conditions.append((
            grid[r-1][c-1] == 'M',
            grid[r+1][c-1] == 'M',
            grid[r-1][c+1] == 'S',
            grid[r+1][c+1] == 'S',
        ))

        conditions.append((
            grid[r-1][c-1] == 'S',
            grid[r+1][c-1] == 'S',
            grid[r-1][c+1] == 'M',
            grid[r+1][c+1] == 'M',
        ))

        conditions.append((
            grid[r+1][c-1] == 'M',
            grid[r+1][c+1] == 'M',
            grid[r-1][c-1] == 'S',
            grid[r-1][c+1] == 'S',
        ))
        conditions.append((
            grid[r+1][c-1] == 'S',
            grid[r+1][c+1] == 'S',
            grid[r-1][c-1] == 'M',
            grid[r-1][c+1] == 'M',
        ))

    for condition in conditions:
        if all(condition):
            new_grid[r][c] = 'A'
            new_grid[r-1][c-1] = 'M'
            new_grid[r+1][c-1] = 'M'
            new_grid[r-1][c+1] = 'S'
            new_grid[r+1][c+1] = 'S'
            xmas_count += 1


# pretty print new grid
for row in new_grid:
    print(''.join(row))

print(xmas_count)
