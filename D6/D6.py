import functools
import math

import lib

lines = lib.split_file('input.txt', '\n')
lines = [line[0].split()[1:] for line in lines]

# P1
total = 1
for i in range(len(lines[0])):
    T = int(lines[0][i])
    d = int(lines[1][i])
    sol0 = math.ceil((T - math.sqrt(T ** 2 - 4 * d)) / 2)
    sol1 = math.floor((T + math.sqrt(T ** 2 - 4 * d)) / 2)
    if (T - sol0) * sol0 == d:
        sol0 += 1
    if (T - sol1) * sol1 == d:
        sol1 -= 1
    total *= sol1 - sol0 + 1
print(total)

# P2
T = int(functools.reduce(lambda a, b: a+b, lines[0]))
d = int(functools.reduce(lambda a, b: a+b, lines[1]))
sol0 = math.ceil((T - math.sqrt(T ** 2 - 4 * d)) / 2)
sol1 = math.floor((T + math.sqrt(T ** 2 - 4 * d)) / 2)
if (T - sol0) * sol0 == d:
    sol0 += 1
if (T - sol1) * sol1 == d:
    sol1 -= 1
print(sol1 - sol0 + 1)
