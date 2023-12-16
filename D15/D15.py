import lib

codes = lib.split_file('input.txt', ',')[0]

# P1
total = 0
for code in codes:
    hashed = 0
    for c in code:
        hashed += ord(c)
        hashed *= 17
        hashed %= 256
    total += hashed
print(total)

# P2
boxes = [[] for i in range(256)]
for code in codes:
    if '-' in code:
        label = code[:-1]
        op = '-'
    else:
        segs = code.split('=')
        label = segs[0]
        focal = int(segs[1])
        op = '='
    hashed = 0
    for c in label:
        hashed += ord(c)
        hashed *= 17
        hashed %= 256
    if '-' == op:
        ind = [i for i, x in enumerate(boxes[hashed]) if x[0] == label]
        if len(ind) > 0:
            del boxes[hashed][ind[0]]
    else:
        ind = [i for i, x in enumerate(boxes[hashed]) if x[0] == label]
        if len(ind) > 0:
            boxes[hashed][ind[0]] = (label, focal)
        else:
            boxes[hashed].append((label, focal))

total = 0
for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        total += (i + 1) * (j + 1) * lens[1]

print(total)
