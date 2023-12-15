import lib

lines = lib.split_file('input.txt', '\n')
lines = [line[0] for line in lines]
line_segs = list(zip(*[line.split() for line in lines]))
springs = line_segs[0]
codes = line_segs[1]
codes = [[int(c) for c in code.split(',')] for code in codes]


def count(spring, structure, groups, contiguous):
    if len(structure) == 0:
        return len(groups) == 0 or (len(groups) == 1 and contiguous == groups[-1])
    elif structure[0] == '?':
        if len(groups) == 0:
            return count(spring + '.', structure[1:], groups, 0)
        elif contiguous == 0 or contiguous == -1:
            c = count(spring + '.', structure[1:], groups, 0)
            if len(groups) > 0 and contiguous != -1:
                c += count(spring + '#', structure[1:], groups, 1)
            return c
        elif contiguous == groups[0]:
            return count(spring + '.', structure[1:], groups[1:], 0)
        else:
            return count(spring + '#', structure[1:], groups, contiguous + 1)
    elif contiguous != -1 and sum(groups) - contiguous > sum(c == '?' or c == '#' for c in structure):
        return 0
    elif structure[0] == '#':
        if contiguous == -1 or len(groups) == 0:
            return 0
        elif contiguous + 1 < groups[0]:
            return count(spring + '#', structure[1:], groups, contiguous + 1)
        elif contiguous + 1 == groups[0]:
            return count(spring + '#', structure[1:], groups[1:], -1)
        else:
            return 0
    else:
        if contiguous <= 0:
            return count(spring + '.', structure[1:], groups, 0)
        elif contiguous == groups[0]:
            return count(spring + '.', structure[1:], groups[1:], 0)
        else:
            return 0


total = 0
for spring, code in zip(springs, codes):
    total += count('', spring, code, 0)
print(total)

# P2
# If ends with # then there is no benefit
total = 0
for spring, code in zip(springs, codes):
    c = count('', spring, code, 0)
    if spring[-1] == '#':
        total += c ** 5
    elif count('', spring + '?', code, 0) > c:
        total += c * count('', spring + '?', code, 0) ** 4
    elif count('', '?' + spring, code, 0) > c:
        total += c * count('', '?' + spring, code, 0) ** 4
    else:
        total += c ** 5
print(total)

spring = '.?????...?'
code = [1, 1, 1]
print(count('', '?'.join([spring] * 5), code * 5, 0))
c = count('', spring, code, 0)
if spring[-1] == '#':
    print(c ** 5)
elif count('', spring + '?', code, 0) > c:
    print(c * count('', spring + '?', code, 0) ** 4)
elif count('', '?' + spring, code, 0) > c:
    print(c * count('', '?' + spring, code, 0) ** 4)
else:
    print(c ** 5)
