import math

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

import lib

grid = lib.file_to_mat('input.txt')

# P1
dist = np.full(grid.shape, np.inf)

dist[grid == 'S'] = 0
locs = [(np.argwhere(grid == 'S')[0], 0)]
nstep = 65

while len(locs) > 0:
    loc, steps = locs.pop()
    if steps < nstep:
        neighbors = lib.neighbors4(grid, loc[0], loc[1])
        for neighbor in neighbors:
            if grid[neighbor[0], neighbor[1]] == '.':
                if steps + 1 < dist[neighbor[0], neighbor[1]]:
                    locs.append((neighbor, steps + 1))
                    dist[neighbor[0], neighbor[1]] = steps + 1

even_diamond = np.nansum(dist % 2 == 0)
odd_diamond = np.nansum(dist % 2 == 1)
print(even_diamond)

# P2
steps = 26501365
n = steps // 131
tiles = (2 * n + 1) ** 2
print(((tiles - 1) / 2 + 1) * odd_diamond + (tiles - 1) / 2 * even_diamond - 4 * (n / 2) * (3 * (n / 2 + 1) - 64))
