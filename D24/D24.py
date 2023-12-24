import sympy as sp

import lib

lines = lib.split_file('input.txt', '\n')
lines = [line[0] for line in lines]
starts = [[int(p) for p in line.split(' @ ')[0].split(', ')] for line in lines]
velocities = [[int(p) for p in line.split(' @ ')[1].split(', ')] for line in lines]

# P1
min_pos = 200000000000000
max_pos = 400000000000000

did_cross = 0
for i in range(len(starts)):
    for j in range(i + 1, len(starts)):
        asx = starts[i][0]
        asy = starts[i][1]
        adx = velocities[i][0]
        ady = velocities[i][1]
        bsx = starts[j][0]
        bsy = starts[j][1]
        bdx = velocities[j][0]
        bdy = velocities[j][1]
        dx = bsx - asx
        dy = bsy - asy
        det = bdx * ady - bdy * adx
        if det != 0:
            u = (dy * bdx - dx * bdy) / det
            v = (dy * adx - dx * ady) / det
            if u > 0 and v > 0:
                px = asx + adx * u
                py = asy + ady * u
                if min_pos <= px <= max_pos and min_pos <= py <= max_pos:
                    did_cross += 1

print(did_cross)

# P2
a, b, c, x, y, z, t1, t2, t3, t4 = sp.symbols('a, b, c, x , y, z, t1, t2, t3, t4')
eq = [sp.Eq(x + t1 * a, starts[0][0] + t1 * velocities[0][0]), sp.Eq(y + t1 * b, starts[0][1] + t1 * velocities[0][1]),
      sp.Eq(z + t1 * c, starts[0][2] + t1 * velocities[0][2]), sp.Eq(x + t2 * a, starts[1][0] + t2 * velocities[1][0]),
      sp.Eq(y + t2 * b, starts[1][1] + t2 * velocities[1][1]), sp.Eq(z + t2 * c, starts[1][2] + t2 * velocities[1][2]),
      sp.Eq(x + t3 * a, starts[2][0] + t3 * velocities[2][0]), sp.Eq(y + t3 * b, starts[2][1] + t3 * velocities[2][1]),
      sp.Eq(z + t3 * c, starts[2][2] + t3 * velocities[2][2]), sp.Eq(x + t4 * a, starts[3][0] + t4 * velocities[3][0]),
      sp.Eq(y + t4 * b, starts[3][1] + t4 * velocities[3][1]), sp.Eq(z + t4 * c, starts[3][2] + t4 * velocities[3][2])]
output = sp.solve(eq, dict=True)

print(output[0][x] + output[0][y] + output[0][z])
