import lib

lines = lib.split_file('input.txt', '\n')
lines = [line[0] for line in lines]

# P1
seeds = [int(e) for e in lines[0].split(' ')[1:]]
maps = [lines[lines.index('seed-to-soil map:')+1:lines.index('soil-to-fertilizer map:')-1],
        lines[lines.index('soil-to-fertilizer map:')+1:lines.index('fertilizer-to-water map:')-1],
        lines[lines.index('fertilizer-to-water map:')+1:lines.index('water-to-light map:')-1],
        lines[lines.index('water-to-light map:')+1:lines.index('light-to-temperature map:')-1],
        lines[lines.index('light-to-temperature map:')+1:lines.index('temperature-to-humidity map:')-1],
        lines[lines.index('temperature-to-humidity map:')+1:lines.index('humidity-to-location map:')-1],
        lines[lines.index('humidity-to-location map:')+1:]]

locations = []
for seed in seeds:
    value = seed
    for m in maps:
        for entry in m:
            seq = [int(e) for e in entry.split(' ')]
            if seq[1] <= value <= seq[1] + seq[2] - 1:
                value = value - seq[1] + seq[0]
                break
    locations.append(value)

print(min(locations))

# P2
ranges = list(zip(seeds[0::2], seeds[1::2]))
ranges = [(r[0], r[0] + r[1] - 1) for r in ranges]
for m in maps:
    new_ranges = []
    ind = 0
    while ind < len(ranges):
        cur_range = ranges[ind]
        trans_range = ranges[ind]
        complete = False
        for entry in m:
            seq = [int(e) for e in entry.split(' ')]
            if seq[1] <= trans_range[0] <= seq[1] + seq[2] - 1:
                end_range = min(trans_range[1] - seq[1] + seq[0], seq[0] + seq[2] - 1)
                new_ranges.append((trans_range[0] - seq[1] + seq[0], end_range))
                if end_range == trans_range[1] - seq[1] + seq[0]:
                    complete = True
                    break
                else:
                    trans_range = (seq[1] + seq[2], trans_range[1])
            elif seq[1] <= trans_range[1] <= seq[1] + seq[2] - 1:
                start_range = max(trans_range[1] - seq[2] + 1, seq[1]) - seq[1] + seq[0]
                new_ranges.append((start_range, trans_range[1] - seq[1] + seq[0]))
                if start_range == trans_range[1] - seq[2] + 1:
                    complete = True
                    break
                else:
                    trans_range = (trans_range[0], seq[1] - 1)
            elif seq[1] >= trans_range[0] and seq[1] + seq[2] - 1 <= trans_range[1]:
                new_ranges.append((seq[0], seq[0] + seq[2] - 1))
                if seq[1] + seq[2] - 1 < trans_range[1]:
                    ranges.append((seq[1] + seq[2], trans_range[1]))
                if seq[1] > trans_range[0]:
                    trans_range = (trans_range[0], seq[1] - 1)
                else:
                    complete = True
        if not complete:
            new_ranges.append(trans_range)
        ind += 1
    ranges = new_ranges
print(min(r[0] for r in ranges))
