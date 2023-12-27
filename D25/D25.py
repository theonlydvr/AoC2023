import lib
import networkx as nx

lines = lib.split_file('input.txt', '\n')
lines = [line[0] for line in lines]

G = nx.Graph()
for line in lines:
    segs = line.split(': ')
    for dest in segs[1].split(' '):
        G.add_edge(segs[0], dest)

# P1
cut = nx.minimum_edge_cut(G)
for e in cut:
    G.remove_edge(e[0], e[1])
components = [G.subgraph(c).copy() for c in nx.connected_components(G)]
print(len(components[0]) * len(components[1]))
