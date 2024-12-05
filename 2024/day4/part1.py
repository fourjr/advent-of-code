import aoc
import numpy as np


rows = aoc.get_input(sep='\n')
grid = np.array([list(row) for row in rows])
xmas_count = 0
new_grid = np.zeros(grid.shape, dtype=str)
new_grid.fill('.')
for r, c in np.argwhere(grid == 'X'):
    conditions = []
    # X
    # M
    # A
    # S
    if r + 3 < grid.shape[0]:
        conditions.append((
            grid[r+1][c] == 'M',
            grid[r+2][c] == 'A',
            grid[r+3][c] == 'S',
        ))
        if all(conditions[-1]):
            new_grid[r][c] = 'X'
            new_grid[r+1][c] = 'M'
            new_grid[r+2][c] = 'A'
            new_grid[r+3][c] = 'S'
    # X M A S
    if c + 3 < grid.shape[1]:
        conditions.append((
            grid[r][c+1] == 'M',
            grid[r][c+2] == 'A',
            grid[r][c+3] == 'S',
        ))
        if all(conditions[-1]):
            new_grid[r][c] = 'X'
            new_grid[r][c+1] = 'M'
            new_grid[r][c+2] = 'A'
            new_grid[r][c+3] = 'S'
    # S A M X
    if c - 3 >= 0:
        conditions.append((
            grid[r][c-1] == 'M',
            grid[r][c-2] == 'A',
            grid[r][c-3] == 'S',
        ))
        if all(conditions[-1]):
            new_grid[r][c] = 'X'
            new_grid[r][c-1] = 'M'
            new_grid[r][c-2] = 'A'
            new_grid[r][c-3] = 'S'
    # S
    # A
    # M
    # X
    if r - 3 >= 0:
        conditions.append((
            grid[r-1][c] == 'M',
            grid[r-2][c] == 'A',
            grid[r-3][c] == 'S',
        ))
        if all(conditions[-1]):
            new_grid[r][c] = 'X'
            new_grid[r-1][c] = 'M'
            new_grid[r-2][c] = 'A'
            new_grid[r-3][c] = 'S'
    # SW Diagonal XMAS
    if r + 3 < grid.shape[0] and c + 3 < grid.shape[1]:
        conditions.append((
            grid[r+1][c+1] == 'M',
            grid[r+2][c+2] == 'A',
            grid[r+3][c+3] == 'S',
        ))
        if all(conditions[-1]):
            new_grid[r][c] = 'X'
            new_grid[r+1][c+1] = 'M'
            new_grid[r+2][c+2] = 'A'
            new_grid[r+3][c+3] = 'S'
    # NW Diagonal XMAS
    if r - 3 >= 0 and c + 3 < grid.shape[1]:
        conditions.append((
            grid[r-1][c+1] == 'M',
            grid[r-2][c+2] == 'A',
            grid[r-3][c+3] == 'S',
        ))
        if all(conditions[-1]):
            new_grid[r][c] = 'X'
            new_grid[r-1][c+1] = 'M'
            new_grid[r-2][c+2] = 'A'
            new_grid[r-3][c+3] = 'S'
    # NE Diagonal XMAS
    if r - 3 >= 0 and c - 3 >= 0:
        conditions.append((
            grid[r-1][c-1] == 'M',
            grid[r-2][c-2] == 'A',
            grid[r-3][c-3] == 'S',
        ))
        if all(conditions[-1]):
            new_grid[r][c] = 'X'
            new_grid[r-1][c-1] = 'M'
            new_grid[r-2][c-2] = 'A'
            new_grid[r-3][c-3] = 'S'
    # SE Diagonal XMAS
    if r + 3 < grid.shape[0] and c - 3 >= 0:
        conditions.append((
            grid[r+1][c-1] == 'M',
            grid[r+2][c-2] == 'A',
            grid[r+3][c-3] == 'S',
        ))
        if all(conditions[-1]):
            new_grid[r][c] = 'X'
            new_grid[r+1][c-1] = 'M'
            new_grid[r+2][c-2] = 'A'
            new_grid[r+3][c-3] = 'S'

    for condition in conditions:
        if all(condition):
            xmas_count += 1


# pretty print new grid
for row in new_grid:
    print(''.join(row))

print(xmas_count)
