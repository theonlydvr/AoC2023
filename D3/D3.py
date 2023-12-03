import lib

schematic = lib.file_to_list2('input.txt')

# P1
total = 0
for row in range(len(schematic)):
    num = ''
    col = 0
    while col < len(schematic[row]):
        if str.isdigit(schematic[row][col]):
            begin = col - 1
            while col < len(schematic) and str.isdigit(schematic[row][col]):
                num += schematic[row][col]
                col += 1
            cols = list(range(begin, col + 1))
            rows = list(range(row - 1, row + 2))
            valid = False
            for r in rows:
                if 0 <= r < len(schematic):
                    for c in cols:
                        if 0 <= c < len(schematic[r]):
                            if schematic[r][c] != '.' and not str.isdigit(schematic[r][c]):
                                total += int(num)
                                valid = True
                                break
                if valid:
                    break
            num = ''
        col += 1
print(total)

# P2
gears = {}
for row in range(len(schematic)):
    num = ''
    col = 0
    while col < len(schematic[row]):
        if str.isdigit(schematic[row][col]):
            begin = col - 1
            while col < len(schematic) and str.isdigit(schematic[row][col]):
                num += schematic[row][col]
                col += 1
            cols = list(range(begin, col + 1))
            rows = list(range(row - 1, row + 2))
            valid = False
            for r in rows:
                if 0 <= r < len(schematic):
                    for c in cols:
                        if 0 <= c < len(schematic[r]):
                            if schematic[r][c] == '*':
                                if (r, c) not in gears:
                                    gears[(r, c)] = []
                                gears[(r, c)].append(int(num))
                                valid = True
                                break
                if valid:
                    break
            num = ''
        col += 1
total = 0
for nums in gears.values():
    if len(nums) == 2:
        total += nums[0] * nums[1]
print(total)
