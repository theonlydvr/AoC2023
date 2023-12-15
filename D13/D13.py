import numpy as np

import lib

segs = lib.split_file('input.txt', '\n')
grid = []
grids = []
for line in segs:
    if len(line[0]) == 0:
        grids.append(np.asarray(grid))
        grid = []
    else:
        grid.append([c for c in line[0]])
grids.append(np.asarray(grid))

# P1
total = 0
for grid in grids:
    for r in range(1, grid.shape[0]):
        if r < grid.shape[0] / 2 and np.all(grid[:r, :] == np.flip(grid[r:2*r, :], axis=0)):
            total += 100 * r
        elif r > grid.shape[0] / 2 and np.all(grid[r:, :] == np.flip(grid[2*r-grid.shape[0]:r, :], axis=0)):
            total += 100 * r
    for c in range(1, grid.shape[1]):
        if c < grid.shape[1] / 2 and np.all(grid[:, :c] == np.flip(grid[:, c:2*c], axis=1)):
            total += c
        elif c > grid.shape[1] / 2 and np.all(grid[:, c:] == np.flip(grid[:, 2*c-grid.shape[1]:c], axis=1)):
            total += c

print(total)

# P2
total = 0
for grid in grids:
    for r in range(1, grid.shape[0]):
        if r < grid.shape[0] / 2 and np.sum(grid[:r, :] != np.flip(grid[r:2*r, :], axis=0)) == 1:
            total += 100 * r
        elif r > grid.shape[0] / 2 and np.sum(grid[r:, :] != np.flip(grid[2*r-grid.shape[0]:r, :], axis=0)) == 1:
            total += 100 * r
    for c in range(1, grid.shape[1]):
        if c < grid.shape[1] / 2 and np.sum(grid[:, :c] != np.flip(grid[:, c:2*c], axis=1)) == 1:
            total += c
        elif c > grid.shape[1] / 2 and np.sum(grid[:, c:] != np.flip(grid[:, 2*c-grid.shape[1]:c], axis=1)) == 1:
            total += c

print(total)
