#!/usr/bin/env python3

import re
from functools import reduce
from operator import and_

from aoc import read_input

def get_map(foods, algs):
    possbl = [(a, set(reduce(and_, (set(ingrs) for (ingrs, algs) in foods if a in algs)))) for a in algs]
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

raw = [row.split(' (contains ') for row in read_input(2020, 21).split('\n')[:-1]]
foods = list(map(lambda row: (re.findall(r'\w+', row[0]), re.findall(r'\w+', row[1])), raw))
allergens  = list(set([allergen for (_, allergens) in foods for allergen in allergens]))
map_ = get_map(foods, allergens)

print(f"Puzzle 1: {puzzle1(foods, map_)}")
print(f"Puzzle 2: {puzzle2(map_)}")