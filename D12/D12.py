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
segs = {}


def count2(structure, groups, contiguous, rem, begin):
    if len(structure) == 0:
        if len(rem) == 0 and len(groups) == 1 and contiguous == groups[-1]:
            groups = []
            contiguous = 0
        if len(rem) > 0 or len(groups) == 0:
            if (str(groups), contiguous) in segs:
                segs[(str(groups), contiguous)] += begin
            else:
                segs[(str(groups), contiguous)] = begin
    elif structure[0] == '?':
        if len(groups) == 0:
            count2(structure[1:], groups, 0, rem, begin)
        elif contiguous == 0 or contiguous == -1:
            count2(structure[1:], groups, 0, rem, begin)
            if len(groups) > 0 and contiguous != -1:
                count2(structure[1:], groups, 1, rem, begin)
        elif contiguous == groups[0]:
            count2(structure[1:], groups[1:], 0, rem, begin)
        else:
            count2(structure[1:], groups, contiguous + 1, rem, begin)
    elif contiguous != -1 and sum(groups) - contiguous > sum(c == '?' or c == '#' for c in structure + rem):
        return
    elif structure[0] == '#':
        if contiguous == -1 or len(groups) == 0:
            return
        elif contiguous + 1 < groups[0]:
            count2(structure[1:], groups, contiguous + 1, rem, begin)
        elif contiguous + 1 == groups[0]:
            count2(structure[1:], groups[1:], -1, rem, begin)
        else:
            return
    else:
        if contiguous <= 0:
            count2(structure[1:], groups, 0, rem, begin)
        elif contiguous == groups[0]:
            count2(structure[1:], groups[1:], 0, rem, begin)
        else:
            return


total = 0
for spring, code in zip(springs, codes):
    segs = {}
    count2(spring, code * 5, 0, '?' + '?'.join([spring] * 4), 1)
    for i in range(4):
        prev_segs = segs.copy()
        segs = {}
        for key, val in prev_segs.items():
            if i < 3:
                count2('?' + spring, eval(key[0]), key[1], '?' + '?'.join([spring] * (3 - i)), val)
            else:
                count2('?' + spring, eval(key[0]), key[1], '', val)
    if ('[]', 0) in segs:
        total += segs[('[]', 0)]
    elif ('[]', -1) in segs:
        total += segs[('[]', -1)]

print(total)
