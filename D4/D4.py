import lib

lines = lib.split_file('input.txt', delim='\n')
lines = [line[0].split(':')[1] for line in lines]

# P1
cards = [line.split(' | ') for line in lines]
total = 0
for card in cards:
    winning = card[0].split()
    drawn = card[1].split()
    intersection = [val for val in winning if val in drawn]
    if len(intersection) > 0:
        total += 2 ** (len([val for val in winning if val in drawn]) - 1)

print(total)

# P2
nmatch = []


def count_copies(ind):
    if ind < len(nmatch):
        return 1 + sum(count_copies(i) for i in range(ind + 1, ind + nmatch[ind] + 1))
    else:
        return 0


for card in cards:
    winning = card[0].split()
    drawn = card[1].split()
    intersection = [val for val in winning if val in drawn]
    nmatch.append(len(intersection))
total = sum(count_copies(ind) for ind in range(len(nmatch)))
print(total)
