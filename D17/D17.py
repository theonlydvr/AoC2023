import heapq

import lib

grid = lib.file_to_mat('input.txt')

# P1
nodes = [lib.PrioritizedItem(0, ((0, 0), 0, None))]
directions = [[{} for i in range(grid.shape[1])] for j in range(grid.shape[0])]
for i in range(3):
    directions[0][0].update({(1, 0, i + 1): 0, (-1, 0, i + 1): 0, (0, 1, i + 1): 0, (0, -1, i + 1): 0})

while len(nodes) > 0:
    item = heapq.heappop(nodes)
    neighbors = lib.neighbors4(grid, item.item[0][0], item.item[0][1])
    if item.item[2] is not None and (item.item[0][0] - item.item[2][0], item.item[0][1] - item.item[2][1]) in neighbors:
        neighbors.remove((item.item[0][0] - item.item[2][0], item.item[0][1] - item.item[2][1]))
    for neighbor in neighbors:
        if item.item[2] is None or (item.item[0][0] + item.item[2][0], item.item[0][1] + item.item[2][1]) != neighbor:
            drc = (neighbor[0] - item.item[0][0], neighbor[1] - item.item[0][1])
            if (drc[0], drc[1], 1) not in directions[neighbor[0]][neighbor[1]] \
                    or item.priority + grid[neighbor[0], neighbor[1]] < directions[neighbor[0]][neighbor[1]][(drc[0], drc[1], 1)]:
                directions[neighbor[0]][neighbor[1]][(drc[0], drc[1], 1)] = item.priority + grid[neighbor[0], neighbor[1]]
                heapq.heappush(nodes, lib.PrioritizedItem(directions[neighbor[0]][neighbor[1]][(drc[0], drc[1], 1)], (neighbor, 1, drc)))
        elif item.item[1] < 3:
            drc = item.item[2]
            if (drc[0], drc[1], item.item[1] + 1) not in directions[neighbor[0]][neighbor[1]] \
                    or item.priority + grid[neighbor[0], neighbor[1]] < directions[neighbor[0]][neighbor[1]][(drc[0], drc[1], item.item[1] + 1)]:
                directions[neighbor[0]][neighbor[1]][(drc[0], drc[1], item.item[1] + 1)] = item.priority + grid[neighbor[0], neighbor[1]]
                heapq.heappush(nodes, lib.PrioritizedItem(directions[neighbor[0]][neighbor[1]][(drc[0], drc[1], item.item[1] + 1)], (neighbor, item.item[1] + 1, drc)))
    if len(directions[-1][-1]) > 0:
        best = min(directions[-1][-1].values())
        if all(node.priority > best for node in nodes):
            break

# heat = np.full(grid.shape, np.inf)
# for i in range(heat.shape[0]):
#     for j in range(heat.shape[1]):
#         heat[i, j] = min(directions[i][j].values())
print(min(directions[-1][-1].values()))

# P2
nodes = [lib.PrioritizedItem(0, ((0, 0), 0, None))]
directions = [[{} for i in range(grid.shape[1])] for j in range(grid.shape[0])]
for i in range(10):
    directions[0][0].update({(1, 0, i + 1): 0, (-1, 0, i + 1): 0, (0, 1, i + 1): 0, (0, -1, i + 1): 0})

while len(nodes) > 0:
    item = heapq.heappop(nodes)
    neighbors = lib.neighbors4(grid, item.item[0][0], item.item[0][1])
    if item.item[2] is not None:
        if (item.item[0][0] - item.item[2][0], item.item[0][1] - item.item[2][1]) in neighbors:
            neighbors.remove((item.item[0][0] - item.item[2][0], item.item[0][1] - item.item[2][1]))
        if item.item[1] < 4:
            if (item.item[0][0] - item.item[2][1], item.item[0][1] - item.item[2][0]) in neighbors:
                neighbors.remove((item.item[0][0] - item.item[2][1], item.item[0][1] - item.item[2][0]))
            if (item.item[0][0] + item.item[2][1], item.item[0][1] + item.item[2][0]) in neighbors:
                neighbors.remove((item.item[0][0] + item.item[2][1], item.item[0][1] + item.item[2][0]))
    for neighbor in neighbors:
        if item.item[2] is None or (item.item[0][0] + item.item[2][0], item.item[0][1] + item.item[2][1]) != neighbor:
            drc = (neighbor[0] - item.item[0][0], neighbor[1] - item.item[0][1])
            if (drc[0], drc[1], 1) not in directions[neighbor[0]][neighbor[1]] \
                    or item.priority + grid[neighbor[0], neighbor[1]] < directions[neighbor[0]][neighbor[1]][(drc[0], drc[1], 1)]:
                directions[neighbor[0]][neighbor[1]][(drc[0], drc[1], 1)] = item.priority + grid[neighbor[0], neighbor[1]]
                heapq.heappush(nodes, lib.PrioritizedItem(directions[neighbor[0]][neighbor[1]][(drc[0], drc[1], 1)], (neighbor, 1, drc)))
        elif item.item[1] < 10:
            drc = item.item[2]
            if (drc[0], drc[1], item.item[1] + 1) not in directions[neighbor[0]][neighbor[1]] \
                    or item.priority + grid[neighbor[0], neighbor[1]] < directions[neighbor[0]][neighbor[1]][(drc[0], drc[1], item.item[1] + 1)]:
                directions[neighbor[0]][neighbor[1]][(drc[0], drc[1], item.item[1] + 1)] = item.priority + grid[neighbor[0], neighbor[1]]
                heapq.heappush(nodes, lib.PrioritizedItem(directions[neighbor[0]][neighbor[1]][(drc[0], drc[1], item.item[1] + 1)], (neighbor, item.item[1] + 1, drc)))
    if len(directions[-1][-1]) > 0:
        valid = [directions[-1][-1][key] for key in directions[-1][-1] if key[-1] >= 4]
        if len(valid) > 0:
            best = min(valid)
            if all(node.priority > best for node in nodes):
                break

# heat = np.full(grid.shape, np.inf)
# for i in range(heat.shape[0]):
#     for j in range(heat.shape[1]):
#         valid = [directions[-1][-1][key] for key in directions[-1][-1] if key[-1] >= 4]
#         if len(valid) > 0:
#             heat[i, j] = min(valid)
print(min(directions[-1][-1][key] for key in directions[-1][-1] if key[-1] >= 4))
