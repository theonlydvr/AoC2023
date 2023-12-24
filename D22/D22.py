import numpy as np

import lib

lines = lib.split_file('input.txt', '\n')
lines = [line[0] for line in lines]
starts = [line.split('~')[0].split(',') for line in lines]
starts = np.asarray(starts).astype(int)
ends = [line.split('~')[1].split(',') for line in lines]
ends = np.asarray(ends).astype(int)
shape = np.max(ends, axis=0)

# P1
stuck = np.zeros(shape + 1)
stuck[:, :, 0] = -1
bricks = list(range(starts.shape[0]))
supported = {}
while len(bricks) > 0:
    changed = True
    while changed:
        changed = False
        new_bricks = []
        for brick in bricks:
            seg = ends[brick, :] - starts[brick, :]
            b_len = np.max(seg)
            b_dir = seg // max(b_len, 1)
            pos = np.copy(starts[brick, :])
            dropped = False
            for i in range(b_len + 1):
                if stuck[pos[0], pos[1], pos[2] - 1]:
                    changed = True
                    pos2 = np.copy(starts[brick, :])
                    for j in range(b_len + 1):
                        stuck[pos2[0], pos2[1], pos2[2]] = brick + 1
                        pos2 += b_dir
                    dropped = True
                    break
                pos += b_dir
            if not dropped:
                new_bricks.append(brick)
        bricks = new_bricks
    for brick in bricks:
        ends[brick, 2] -= 1
        starts[brick, 2] -= 1


bricks = list(range(starts.shape[0]))
for brick in bricks:
    supported[brick + 1] = set()
    seg = ends[brick, :] - starts[brick, :]
    b_len = np.max(seg)
    b_dir = seg // max(b_len, 1)
    pos = np.copy(starts[brick, :])
    for i in range(b_len + 1):
        if stuck[pos[0], pos[1], pos[2] - 1] != 0 and stuck[pos[0], pos[1], pos[2] - 1] != brick + 1:
            supported[brick + 1].add(stuck[pos[0], pos[1], pos[2] - 1])
        pos += b_dir

total = 0
for brick in bricks:
    valid = True
    for brick2 in bricks:
        if brick + 1 in supported[brick2 + 1] and len(supported[brick2 + 1]) == 1:
            valid = False
            break
    total += valid
print(total)

# P2
total = 0
for brick in bricks:
    unstable = {brick}
    changed = True
    while changed:
        changed = False
        for brick2 in bricks:
            if brick2 not in unstable and sum(b + 1 in supported[brick2 + 1] for b in unstable) == len(supported[brick2 + 1]):
                unstable.add(brick2)
                changed = True
    total += len(unstable) - 1

print(total)
