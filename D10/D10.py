import numpy as np

import lib

grid = lib.file_to_list2('input.txt')

# P1
distances = -np.ones((len(grid), len(grid[0])))
Sr = [i for i in range(len(grid)) if 'S' in grid[i]][0]
Sc = grid[Sr].index('S')
distances[Sr][Sc] = 0

branches = [(Sr - 1, Sc), (Sr, Sc + 1)]
# branches = [(Sr + 1, Sc), (Sr, Sc - 1)]
for branch in branches:
    prev = (Sr, Sc)
    steps = 0
    pos = branch
    while True:
        steps += 1
        if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
            if distances[pos[0]][pos[1]] == -1 or distances[pos[0]][pos[1]] > steps:
                distances[pos[0]][pos[1]] = steps
                pos_t = pos
                if grid[pos[0]][pos[1]] == '|':
                    pos = (pos[0] - 1, pos[1])if prev[0] > pos[0] else (pos[0] + 1, pos[1])
                elif grid[pos[0]][pos[1]] == '-':
                    pos = (pos[0], pos[1] - 1) if prev[1] > pos[1] else (pos[0], pos[1] + 1)
                elif grid[pos[0]][pos[1]] == 'L':
                    pos = (pos[0], pos[1] + 1) if prev[0] < pos[0] else (pos[0] - 1, pos[1])
                elif grid[pos[0]][pos[1]] == 'J':
                    pos = (pos[0], pos[1] - 1) if prev[0] < pos[0] else (pos[0] - 1, pos[1])
                elif grid[pos[0]][pos[1]] == '7':
                    pos = (pos[0], pos[1] - 1) if prev[0] > pos[0] else (pos[0] + 1, pos[1])
                elif grid[pos[0]][pos[1]] == 'F':
                    pos = (pos[0], pos[1] + 1) if prev[0] > pos[0] else (pos[0] + 1, pos[1])
                else:
                    break
                prev = pos_t
            else:
                break
        else:
            break

print(np.max(distances))

# P2
grid[Sr][Sc] = 'J'
inside = np.zeros(distances.shape)
n_inside = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if distances[r][c] == -1:
            crossings = 0
            last = ''
            for i in range(c, len(grid[0])):
                if distances[r][i] != -1:
                    if grid[r][i] == '|':
                        crossings += 1
                        last = grid[r][i]
                    elif grid[r][i] == 'L' or grid[r][i] == 'F':
                        crossings += 1
                        last = grid[r][i]
                    elif grid[r][i] == 'J' and last == 'L':
                        last = grid[r][i]
                        crossings += 1
                    elif grid[r][i] == '7' and last == 'F':
                        last = grid[r][i]
                        crossings += 1
            if crossings % 2 == 1:
                inside[r][c] = 1
                n_inside += 1
print(n_inside)
