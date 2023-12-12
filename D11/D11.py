import numpy as np

import lib

grid = lib.file_to_mat('input.txt')

# P1
grid_ex_x = np.atleast_2d(grid[0, :])

for r in range(1, grid.shape[0]):
    if all(grid[r, :] == '.'):
        grid_ex_x = np.concatenate((grid_ex_x, np.atleast_2d(grid[r, :])))
    grid_ex_x = np.concatenate((grid_ex_x, np.atleast_2d(grid[r, :])))

grid_ex = np.transpose(np.atleast_2d(grid_ex_x[:, 0]))
for c in range(1, grid_ex_x.shape[1]):
    if all(grid_ex_x[:, c] == '.'):
        grid_ex = np.concatenate((grid_ex, np.transpose(np.atleast_2d(grid_ex_x[:, c]))), axis=1)
    grid_ex = np.concatenate((grid_ex, np.transpose(np.atleast_2d(grid_ex_x[:, c]))), axis=1)

galaxies = np.where(grid_ex == '#')
shortest_sum = 0

for i in range(len(galaxies[0])):
    for j in range(i + 1, len(galaxies[0])):
        shortest_sum += abs(galaxies[0][i] - galaxies[0][j]) + abs(galaxies[1][i] - galaxies[1][j])

print(shortest_sum)

# P2
galaxies = np.where(grid == '#')
blank_rows = {i for i in range(grid.shape[0]) if all(grid[i, :] == '.')}
blank_cols = {i for i in range(grid.shape[1]) if all(grid[:, i] == '.')}
m_f = 1000000
shortest_sum = 0

for i in range(len(galaxies[0])):
    for j in range(i + 1, len(galaxies[0])):
        shortest_sum += abs(galaxies[0][i] - galaxies[0][j]) + abs(galaxies[1][i] - galaxies[1][j])
        sr = min(galaxies[0][i], galaxies[0][j])
        er = max(galaxies[0][i], galaxies[0][j])
        sc = min(galaxies[1][i], galaxies[1][j])
        ec = max(galaxies[1][i], galaxies[1][j])
        shortest_sum += (m_f - 1) * len(blank_rows & set(range(sr+1, er))) + (m_f - 1) * len(blank_cols & set(range(sc+1, ec)))

print(shortest_sum)
