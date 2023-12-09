import lib

lines = lib.split_file('input.txt', '\n')
lines = [line[0] for line in lines]

# P1
total = 0
for line in lines:
    histories = [[int(n) for n in line.split()]]
    while not all([n == 0 for n in histories[-1]]):
        histories.append([b - a for a, b in zip(histories[-1][:-1], histories[-1][1:])])
    next_value = 0
    for history in reversed(histories[:-1]):
        next_value = history[-1] + next_value
    total += next_value
print(total)

# P2
total = 0
for line in lines:
    histories = [[int(n) for n in line.split()]]
    while not all([n == 0 for n in histories[-1]]):
        histories.append([b - a for a, b in zip(histories[-1][:-1], histories[-1][1:])])
    prev_value = 0
    for history in reversed(histories[:-1]):
        prev_value = history[0] - prev_value
    total += prev_value
print(total)
