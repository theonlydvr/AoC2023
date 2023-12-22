import copy
import re
from functools import reduce
import lib

lines = lib.split_file('input.txt', '\n')
lines = [line[0] for line in lines]
workflows = {}
parts = []
reading_workflows = True
for line in lines:
    if len(line) == 0:
        reading_workflows = False
    elif reading_workflows:
        name = line.split('{')[0]
        c_strs = line[:-1].split('{')[1].split(',')
        conditions = []
        for condition in c_strs:
            if ':' in condition:
                segs = re.split('[<>]', condition)
                cat = segs[0]
                val, dest = segs[1].split(':')
                val = int(val)
                op = '>' if '>' in condition else '<'
                conditions.append((cat, op, val, dest))
            else:
                conditions.append(condition)
        workflows[name] = conditions
    else:
        part = {}
        for seg in line[1:-1].split(','):
            part[seg.split('=')[0]] = int(seg.split('=')[1])
        parts.append(part)

# P1
total = 0
for part in parts:
    cur_flow = 'in'
    while cur_flow != 'A' and cur_flow != 'R':
        workflow = workflows[cur_flow]
        for condition in workflow:
            if isinstance(condition, tuple):
                cat, op, val, dest = condition
                if op == '>' and part[cat] > val:
                    cur_flow = dest
                    break
                elif op == '<' and part[cat] < val:
                    cur_flow = dest
                    break
            else:
                cur_flow = condition
    if cur_flow == 'A':
        total += sum(part.values())
print(total)


# P2
def traverse_workflow(ranges, workflow):
    if workflow == 'A':
        return reduce(lambda x, y: x * y, [r[1] - r[0] + 1 for r in ranges.values()])
    elif workflow == 'R':
        return 0
    else:
        total = 0
        for condition in workflows[workflow]:
            if isinstance(condition, tuple):
                cat, op, val, dest = condition
                if op == '>' and ranges[cat][1] > val:
                    new_ranges = copy.deepcopy(ranges)
                    new_ranges[cat][0] = val + 1
                    total += traverse_workflow(new_ranges, dest)
                    ranges[cat][1] = val
                elif op == '<' and ranges[cat][0] < val:
                    new_ranges = copy.deepcopy(ranges)
                    new_ranges[cat][1] = val - 1
                    total += traverse_workflow(new_ranges, dest)
                    ranges[cat][0] = val
            else:
                total += traverse_workflow(ranges, condition)
        return total


print(traverse_workflow({'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}, 'in'))
