import numpy as np

import lib

grid = lib.file_to_mat('input.txt')


# P1
def energize(pos0, dir0):
    energized = np.zeros(grid.shape)
    dir_mat = np.full(grid.shape, '', dtype=object)
    beams = [pos0]
    directions = [dir0]

    while len(beams) > 0:
        new_beams = []
        new_directions = []
        for pos, direction in zip(beams, directions):
            if grid[pos[0], pos[1]] == 0 or str(direction) not in dir_mat[pos[0], pos[1]]:
                energized[pos[0], pos[1]] = 1
                dir_mat[pos[0], pos[1]] += str(direction)
                if grid[pos[0], pos[1]] == '/':
                    direction = (-direction[1], -direction[0])
                elif grid[pos[0], pos[1]] == '\\':
                    direction = (direction[1], direction[0])
                elif grid[pos[0], pos[1]] == '-' and direction[0] != 0:
                    if pos[1] + 1 < grid.shape[1]:
                        new_beams.append((pos[0], pos[1] + 1))
                        new_directions.append((0, 1))
                    direction = (0, -1)
                elif grid[pos[0], pos[1]] == '|' and direction[1] != 0:
                    if pos[0] + 1 < grid.shape[0]:
                        new_beams.append((pos[0] + 1, pos[1]))
                        new_directions.append((1, 0))
                    direction = (-1, 0)
                if 0 <= pos[0] + direction[0] < grid.shape[0] and 0 <= pos[1] + direction[1] < grid.shape[1]:
                    new_beams.append((pos[0] + direction[0], pos[1] + direction[1]))
                    new_directions.append(direction)
        beams = new_beams
        directions = new_directions

    return np.sum(energized)


print(energize((0, 0), (0, 1)))

# P2
mx = max(energize((0, i), (1, 0)) for i in range(grid.shape[1]))
mx = max(mx, max(energize((grid.shape[0] - 1, i), (-1, 0)) for i in range(grid.shape[1])))
mx = max(mx, max(energize((i, 0), (0, 1)) for i in range(grid.shape[0])))
mx = max(mx, max(energize((i, grid.shape[1] - 1), (0, -1)) for i in range(grid.shape[0])))
print(mx)
