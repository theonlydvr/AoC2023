import numpy as np

import lib

lines = lib.split_file('input.txt', '\n')
lines = [line[0].split() for line in lines]
directions = [line[0] for line in lines]
counts = [int(line[1]) for line in lines]
colors = [line[2][1:-1] for line in lines]

# P1
pos = None
for d, c in zip(directions, counts):
    if d == 'U':
        d2 = (-1, 0)
    elif d == 'D':
        d2 = (1, 0)
    elif d == 'L':
        d2 = (0, -1)
    else:
        d2 = (0, 1)
    m = 0
    while m < c:
        if pos is None:
            grid = np.full((1, 1), '#')
            pos = [0, 0]
        elif pos[0] + d2[0] < 0:
            new_row = np.full((1, max(1, grid.shape[1])), '.')
            new_row[0, pos[1]] = '#'
            grid = np.concatenate((new_row, grid)) if grid.size > 0 else new_row
        elif pos[0] + d2[0] >= grid.shape[0]:
            new_row = np.full((1, max(1, grid.shape[1])), '.')
            new_row[0, pos[1]] = '#'
            grid = np.concatenate((grid, new_row)) if grid.size > 0 else new_row
            pos[0] += 1
        elif pos[1] + d2[1] < 0:
            new_col = np.full((max(1, grid.shape[0]), 1), '.')
            new_col[pos[0], 0] = '#'
            grid = np.concatenate((new_col, grid), axis=1) if grid.size > 0 else new_col
        elif pos[1] + d2[1] >= grid.shape[1]:
            new_col = np.full((max(1, grid.shape[0]), 1), '.')
            new_col[pos[0], 0] = '#'
            grid = np.concatenate((grid, new_col), axis=1) if grid.size > 0 else new_col
            pos[1] += 1
        else:
            pos = [pos[0] + d2[0], pos[1] + d2[1]]
            grid[pos[0], pos[1]] = '#'
        m += 1

enlarged = np.full((grid.shape[0] + 2, grid.shape[1] + 2), '.')
enlarged[1:-1, 1:-1] = grid

fill_pos = [(0, 0)]
while len(fill_pos) > 0:
    pos = fill_pos.pop()
    enlarged[pos[0], pos[1]] = '%'
    neighbors = lib.neighbors4(enlarged, pos[0], pos[1])
    fill_pos += [n for n in neighbors if enlarged[n[0], n[1]] == '.']

grid = enlarged[1:-1, 1:-1]
print(grid.size - np.sum(grid == '%'))

# P2
directions = [int(color[-1]) for color in colors]
counts = [int(color[1:-1], 16) for color in colors]
pos = [0, 0]
positions = [[0, 0]]
for d, c in zip(directions, counts):
    if d == 0:
        pos[1] += c
    elif d == 1:
        pos[0] -= c
    elif d == 2:
        pos[1] -= c
    else:
        pos[0] += c
    positions.append(pos.copy())
mrow = min(pos[0] for pos in positions)
mcol = min(pos[1] for pos in positions)
positions = [[pos[0] - mrow + 1, pos[1] - mcol] for pos in positions]
area = 0
for s, e in zip(positions[:-1], positions[1:]):
    if e[1] > s[1]:
        area += (e[0]) * (e[1] - s[1])
    elif e[1] < s[1]:
        area += (e[0] - 1) * (e[1] - s[1])
    elif e[0] > s[0]:
        area += e[0] - s[0]

print(abs(area) + 1)
