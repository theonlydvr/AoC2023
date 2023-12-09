import math

import lib

lines = lib.split_file('input.txt', '\n')
lines = [line[0] for line in lines]

# P1
turn_seq = lines[0]
node_map = {}
for line in lines[2:]:
    parts = line.split(' = ')
    node_map[parts[0]] = parts[1][1:-1].split(', ')

node = 'AAA'
seq_pos = 0
steps = 0
while node != 'ZZZ':
    node = node_map[node][0] if turn_seq[seq_pos] == 'L' else node_map[node][1]
    seq_pos = (seq_pos + 1) % len(turn_seq)
    steps += 1
print(steps)

# P2
all_steps = []
nodes = list(filter(lambda n: n[-1] == 'A', node_map.keys()))
for node in nodes:
    seq_pos = 0
    steps = 0
    while node[-1] != 'Z':
        node = node_map[node][0] if turn_seq[seq_pos] == 'L' else node_map[node][1]
        seq_pos = (seq_pos + 1) % len(turn_seq)
        steps += 1
    all_steps.append(steps)
print(math.lcm(*all_steps))
