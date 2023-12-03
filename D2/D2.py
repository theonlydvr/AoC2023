import lib

bag = {'red': 12, 'green': 13, 'blue': 14}
lines = lib.split_file('input.txt', '\n')
lines = [line[0].split(':')[1].split(';') for line in lines]

# P1
nums = [[[int(''.join(filter(str.isdigit, num))) for num in draw.split(',')] for draw in line] for line in lines]
colors = [[[''.join(filter(str.isalpha, num)) for num in draw.split(',')] for draw in line] for line in lines]

total = 0
for i in range(len(lines)):
    if all(all([all([bag[pair[1]] >= pair[0]]) for pair in zip(draw[0], draw[1])]) for draw in zip(nums[i], colors[i])):
        total += i + 1

print(total)

# P2
total = 0
for i in range(len(lines)):
    game_bag = {'red': 0, 'green': 0, 'blue': 0}
    for draw in zip(nums[i], colors[i]):
        for pair in zip(draw[0], draw[1]):
            game_bag[pair[1]] = max(game_bag[pair[1]], pair[0])
    total += game_bag['red'] * game_bag ['green'] * game_bag['blue']

print(total)
