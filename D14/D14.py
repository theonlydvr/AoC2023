import matplotlib
import numpy as np

import lib
import matplotlib.pyplot as plt

grid_temp = lib.file_to_mat('input.txt')

# P1
grid = np.full((grid_temp.shape[0] + 2, grid_temp.shape[1] + 2), '#')
grid[1:-1, 1:-1] = grid_temp


def move_rocks(direction):
    rocks = np.argwhere(grid == 'O')
    stuck = np.full(grid.shape, False)
    stuck[grid == '#'] = True

    while rocks.shape[0] > 0:
        changed = True
        while changed:
            blocked = stuck[rocks[:, 0] + direction[0], rocks[:, 1] + direction[1]]
            stuck[rocks[blocked][:, 0], rocks[blocked][:, 1]] = True
            rocks = rocks[np.logical_not(blocked), :]
            changed = np.any(blocked)
        grid[rocks[:, 0], rocks[:, 1]] = '.'
        rocks = rocks + direction
        grid[rocks[:, 0], rocks[:, 1]] = 'O'


move_rocks(np.asarray([-1, 0]))
rocks = np.argwhere(grid == 'O')
print(sum(grid.shape[0] - rocks[:, 0] - 1))

# P2
grid = np.full((grid_temp.shape[0] + 2, grid_temp.shape[1] + 2), '#')
grid[1:-1, 1:-1] = grid_temp
order = [[-1, 0], [0, -1], [1, 0], [0, 1]]
data = np.zeros((2000, 1))
for i in range(data.shape[0]):
    move_rocks(np.asarray(order[i % 4]))
    rocks = np.argwhere(grid == 'O')
    data[i] = sum(grid.shape[0] - rocks[:, 0] - 1)

matplotlib.use('TkAgg')
fig = plt.figure()
plt.plot(data)
fig.show()

cycle = 36
cycle_vals = np.zeros((cycle, 1))
cycle_vals[np.mod(np.arange((data.shape[0]-cycle), data.shape[0]), cycle)] = data[-cycle:]
print(cycle_vals[(4000000000 - 1) % cycle])
