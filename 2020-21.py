#!/usr/bin/env python3

import re
from pprint import pprint
from itertools import product
from functools import reduce
from operator import and_, or_

from aoc import read_input

def puzzle1():
    pass

def puzzle2():
    pass

raw = [row.split(' (contains ') for row in read_input(2020, 21).split('\n')[:-1]]
data = list(map(lambda row: (re.findall(r'\w+', row[0]), re.findall(r'\w+', row[1])), raw))
ingredients  = list(set([ingredient for (ingredients, _) in data for ingredient in ingredients]))
allergens  = list(set([allergen for (_, allergens) in data for allergen in allergens]))

ai_possible = {allergen:[] for allergen in allergens}
for allergen in allergens:
    ai_possible[allergen] = set(reduce(and_, [set(ingredients) for (ingredients, allergens) in data if allergen in allergens]))

reduced = True
contains = {}
contained = set()
while reduced:
    reduced = False
    for ingr in ai_possible:
        if len(ai_possible[ingr]) == 1:
            reduced = True
            allg, *_ = ai_possible[ingr]
            contains[ingr] = allg
            contained.add(allg)
            for ingr in ai_possible:
                ai_possible[ingr] -= contained

no_allgs = [ingr for ingr in ingredients if ingr not in contained]
occurs_no_alg = [ingr for (ingredients, _) in data for ingr in ingredients if ingr in no_allgs]

dangerous = ','.join([ingr for (ingr, _) in sorted(list(zip(contains.values(), contains.keys())), key=lambda r: r[1])])
print(f"Puzzle 1: {len(occurs_no_alg)}")
print(f"Puzzle 2: {dangerous}")