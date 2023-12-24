import copy

import numpy as np
import networkx as nx

import lib

hiking_map = lib.file_to_mat('input.txt')
start = np.where(hiking_map[0, :] == '.')[0][0]
end = np.where(hiking_map[-1, :] == '.')[0][0]

# P1
paths = [[0, start, set(), None]]
path_len = 0
longest_valid = 0

while len(paths) > 0:
    path_len += 1
    new_paths = []
    for path in paths:
        if path[0] == hiking_map.shape[0] - 1 and path[1] == end:
            longest_valid = path_len
        else:
            if hiking_map[path[0], path[1]] == '.':
                neighbors = lib.neighbors4(hiking_map, path[0], path[1])
            else:
                if hiking_map[path[0], path[1]] == '>':
                    neighbors = [(path[0], path[1] + 1)]
                elif hiking_map[path[0], path[1]] == '<':
                    neighbors = [(path[0], path[1] - 1)]
                elif hiking_map[path[0], path[1]] == '^':
                    neighbors = [(path[0] - 1, path[1])]
                else:
                    neighbors = [(path[0] + 1, path[1])]
            neighbors = [neighbor for neighbor in neighbors if  hiking_map[neighbor[0], neighbor[1]] != '#' and neighbor not in path[2] and neighbor != path[3]]
            for neighbor in neighbors:
                if len(neighbors) > 1:
                    s = path[2].copy()
                    s.add((path[0], path[1]))
                else:
                    s = path[2]
                new_paths.append([neighbor[0], neighbor[1], s, (path[0], path[1])])
    paths = new_paths

print(longest_valid - 1)

# P2
path_len = 0
longest_valid = 0
split_paths = {}
hiking_graph = nx.Graph()


def traverse(pos, prev, origin, path_len):
    while pos[0] != hiking_map.shape[0] - 1 or pos[1] != end:
        neighbors = lib.neighbors4(hiking_map, pos[0], pos[1])
        neighbors = [neighbor for neighbor in neighbors if hiking_map[neighbor[0], neighbor[1]] != '#' and neighbor != prev]
        if len(neighbors) == 1:
            prev = pos
            pos = neighbors[0]
            path_len += 1
        elif pos not in hiking_graph or origin not in hiking_graph[pos]:
            hiking_graph.add_edge(pos, origin, weight=path_len)
            for neighbor in neighbors:
                traverse(neighbor, pos, pos, 1)
            return
        else:
            return
    hiking_graph.add_edge(pos, origin, weight=path_len)


traverse((0, start), None, (0, start), 0)
paths = nx.all_simple_paths(hiking_graph, (0, start), (hiking_map.shape[0] - 1, end))
print(max(nx.path_weight(hiking_graph, path, "weight") for path in paths))
