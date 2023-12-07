#!/usr/bin/env python3

import re

from tools import read_input

def get_map(foods, algs):
    possbl = [(a, set.intersection(*(set(ingrs) for (ingrs, algs) in foods if a in algs))) for a in algs]
    map_ = dict()
    while possbl:
        possbl = sorted(possbl, key=lambda p: -len(p[1]))
        a, (i, *_) = possbl.pop()
        map_[a] = i
        possbl = [(alg,ing - set([i])) for (alg,ing) in possbl]
    return map_

def puzzle1(foods, map_):
    return len([i for (ings, _) in foods for i in ings if i not in map_.values()])

def puzzle2(map_):
    return ','.join(i for (_, i) in sorted(map_.items()))

raw = read_input(2020, 21)
foods = re.findall(r'([^\(]*) \(contains ([^\)]*)\)\n', raw)
foods = [(ingrs.split(), algs.split(', ')) for (ingrs, algs) in foods]
allergens  = list(set([allergen for (_, allergens) in foods for allergen in allergens]))
map_ = get_map(foods, allergens)

print(f"Puzzle 1: {puzzle1(foods, map_)}")
print(f"Puzzle 2: {puzzle2(map_)}")