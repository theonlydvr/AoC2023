import lib

lines = lib.split_file('input.txt')
lines = [line[0] for line in lines]

# P1
just_nums = [''.join(filter(str.isdigit, line)) for line in lines]
print(sum(int(line[0] + line[-1]) for line in just_nums))

# P2

num_strs = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
firsts = []
lasts = []
for line in lines:
    first = ''
    last = ''
    for l in range(len(line)):
        first += line[l]
        last = line[-(l+1)] + last
        for j in range(len(num_strs)):
            first = first.replace(num_strs[j], str(j + 1))
            last = last.replace(num_strs[j], str(j + 1))
    firsts.append(first)
    lasts.append(last)
nums_first = [''.join(filter(str.isdigit, line)) for line in firsts]
nums_last = [''.join(filter(str.isdigit, line)) for line in lasts]
print(sum(int(line[0][0] + line[1][-1]) for line in zip(nums_first, nums_last)))
