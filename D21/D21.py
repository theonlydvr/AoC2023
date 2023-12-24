import numpy as np

import lib

grid = lib.file_to_mat('test.txt')

# P1
dist = np.full(grid.shape, np.inf)

dist[grid == 'S'] = 0
locs = [(np.argwhere(grid == 'S')[0], 0)]
nstep = 64

while len(locs) > 0:
    loc, steps = locs.pop()
    if steps < nstep:
        neighbors = lib.neighbors4(grid, loc[0], loc[1])
        for neighbor in neighbors:
            if grid[neighbor[0], neighbor[1]] == '.':
                if steps + 1 < dist[neighbor[0], neighbor[1]]:
                    locs.append((neighbor, steps + 1))
                    dist[neighbor[0], neighbor[1]] = steps + 1

print(np.nansum(dist % 2 == 0))

# P2
grid = np.tile(grid, (5, 5))
dist = np.full(grid.shape, np.inf)

locs = [(np.argwhere(grid == 'S')[12], 0)]
dist[locs[0][0][0], locs[0][0][1]] = 0

while np.any(dist[grid != '#'] == np.inf) and len(locs) > 0:
    loc, steps = locs.pop(0)
    neighbors = lib.neighbors4(grid, loc[0], loc[1])
    for neighbor in neighbors:
        if grid[neighbor[0], neighbor[1]] == '.':
            if steps + 1 < dist[neighbor[0], neighbor[1]]:
                locs.append((neighbor, steps + 1))
                dist[neighbor[0], neighbor[1]] = steps + 1

dist2 = dist - np.tile(dist[2*grid.shape[0]//5:3*grid.shape[0]//5, 2*grid.shape[1]//5:3*grid.shape[1]//5], (5, 5))
print(np.nansum(dist % 2 == 0))