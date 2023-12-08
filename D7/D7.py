import functools
from collections import Counter

import lib


def hand_strength(hand):
    uniques = Counter(hand)
    counts = list(uniques.values())
    if len(counts) == 1:
        return 7
    elif len(counts) == 2:
        if max(counts) == 4:
            return 6
        else:
            return 5
    elif len(counts) == 3:
        if max(counts) == 3:
            return 4
        else:
            return 3
    elif len(counts) == 4:
        return 2
    return 1


def hand_strength_joker(hand):
    uniques = Counter(hand)
    if 'J' in uniques:
        jokers = uniques['J']
        del uniques['J']
        counts = list(uniques.values())
        if len(counts) == 0:
            counts = [5]
        else:
            counts[counts.index(max(counts))] += jokers
    else:
        counts = list(uniques.values())
    if len(counts) == 1:
        return 7
    elif len(counts) == 2:
        if max(counts) == 4:
            return 6
        else:
            return 5
    elif len(counts) == 3:
        if max(counts) == 3:
            return 4
        else:
            return 3
    elif len(counts) == 4:
        return 2
    return 1


def compare_hands(hand1, hand2, func=hand_strength):
    strength1 = func(hand1)
    strength2 = func(hand2)
    if strength1 == strength2:
        for pair in zip(hand1, hand2):
            val1 = int(pair[0]) if str.isdigit(pair[0]) else value_dict[pair[0]]
            val2 = int(pair[1]) if str.isdigit(pair[1]) else value_dict[pair[1]]
            if val1 != val2:
                return val1 - val2
        return 0
    else:
        return strength1 - strength2


lines = lib.split_file('input.txt', '\n')
lines = [line[0].split() for line in lines]

# P1
cards = [[*line[0]] for line in lines]
values = [int(line[1]) for line in lines]
value_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
value_order = [value for _, value in sorted(zip(cards, values), key=functools.cmp_to_key(lambda a, b: compare_hands(a[0], b[0])))]
print(sum(value * rank for value, rank in zip(value_order, range(1, len(values)+1))))

# P2
value_dict = {'A': 14, 'K': 13, 'Q': 12, 'J': 0, 'T': 10}
value_order = [value for _, value in sorted(zip(cards, values), key=functools.cmp_to_key(lambda a, b: compare_hands(a[0], b[0], func=hand_strength_joker)))]
print(sum(value * rank for value, rank in zip(value_order, range(1, len(values)+1))))
