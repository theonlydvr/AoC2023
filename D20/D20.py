import math

import lib

lines = lib.split_file('input.txt', '\n')
lines = [line[0] for line in lines]

nodes = {}

for line in lines:
    segs = line.split(' -> ')
    name = segs[0][1:]
    if name not in nodes:
        nodes[name] = {'inputs': []}
    nodes[name]['type'] = segs[0][0]
    nodes[name]['outputs'] = segs[1].split(', ')
    if segs[0][0] == '%':
        nodes[name]['state'] = 'low'
    for node in nodes[name]['outputs']:
        if node not in nodes:
            nodes[node] = {'inputs': []}
        nodes[node]['inputs'].append(name)

for node in nodes:
    if 'type' not in nodes[node]:
        nodes[node]['type'] = 'none'
    elif nodes[node]['type'] == '&':
        nodes[node]['state'] = ['low'] * len(nodes[node]['inputs'])

nlow = 0
nhigh = 0
for i in range(1000):
    modules = [('roadcaster', 'low', 'button')]
    for m in modules:
        mdl, pulse, source = m
        if pulse == 'low':
            nlow += 1
        else:
            nhigh += 1
        if nodes[mdl]['type'] == 'b':
            for node in nodes[mdl]['outputs']:
                modules.append((node, 'low', mdl))
        elif nodes[mdl]['type'] == '%' and pulse == 'low':
            if nodes[mdl]['state'] == 'high':
                nodes[mdl]['state'] = 'low'
            else:
                nodes[mdl]['state'] = 'high'
            for node in nodes[mdl]['outputs']:
                modules.append((node, nodes[mdl]['state'], mdl))
        elif nodes[mdl]['type'] == '&':
            nodes[mdl]['state'][nodes[mdl]['inputs'].index(source)] = pulse
            if all(s == 'high' for s in nodes[mdl]['state']):
                output = 'low'
            else:
                output = 'high'
            for node in nodes[mdl]['outputs']:
                modules.append((node, output, mdl))
print(nlow * nhigh)

# P2
nodes = {}

for line in lines:
    segs = line.split(' -> ')
    name = segs[0][1:]
    if name not in nodes:
        nodes[name] = {'inputs': []}
    nodes[name]['type'] = segs[0][0]
    nodes[name]['outputs'] = segs[1].split(', ')
    if segs[0][0] == '%':
        nodes[name]['state'] = 'low'
    for node in nodes[name]['outputs']:
        if node not in nodes:
            nodes[node] = {'inputs': []}
        nodes[node]['inputs'].append(name)

for node in nodes:
    if 'type' not in nodes[node]:
        nodes[node]['type'] = 'none'
    elif nodes[node]['type'] == '&':
        nodes[node]['state'] = ['low'] * len(nodes[node]['inputs'])

total = 0
sent_high = {}
while len(sent_high) < len(nodes) - 2:
    total += 1
    count_rx = 0
    modules = [('roadcaster', 'low', 'button')]
    for m in modules:
        mdl, pulse, source = m
        if pulse == 'high' and source not in sent_high:
            sent_high[source] = total
        if nodes[mdl]['type'] == 'b':
            for node in nodes[mdl]['outputs']:
                modules.append((node, 'low', mdl))
        elif nodes[mdl]['type'] == '%' and pulse == 'low':
            if nodes[mdl]['state'] == 'high':
                nodes[mdl]['state'] = 'low'
            else:
                nodes[mdl]['state'] = 'high'
            for node in nodes[mdl]['outputs']:
                modules.append((node, nodes[mdl]['state'], mdl))
        elif nodes[mdl]['type'] == '&':
            nodes[mdl]['state'][nodes[mdl]['inputs'].index(source)] = pulse
            if all(s == 'high' for s in nodes[mdl]['state']):
                output = 'low'
            else:
                output = 'high'
            for node in nodes[mdl]['outputs']:
                modules.append((node, output, mdl))

print(math.lcm(sent_high['vt'], sent_high['sk'], sent_high['xc'], sent_high['kk']))
