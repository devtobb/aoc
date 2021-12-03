#!/usr/bin/env python3
from copy import deepcopy
from math import prod
from operator import ge, lt

from aoc import read_input

def colsum(raw, col):
    return sum((l[col] for l in raw))

def bin_to_int(l):
    return int("".join(map(str, map(int, l))), 2)

def puzzle1(raw):
    gamma = [colsum(raw, col)>len(raw)/2 for col in range(12)]
    epsilon = [colsum(raw, col)<len(raw)/2 for col in range(12)]
    
    return bin_to_int(gamma) * bin_to_int(epsilon)

def puzzle2(raw):
    result = []
    for op in ge, lt:
        lst = deepcopy(raw)
        col = 0
        while len(lst) > 1:
            lst = list(filter(lambda l: l[col]==op(colsum(lst, col), len(lst)/2), lst))
            col += 1

        remaining, *_ =  lst
        result.append(bin_to_int(remaining))
    
    return prod(result)


raw = read_input(2021, 3)
raw = [[int(e) for e in l] for l in raw.split()]

print(f"Puzzle 1: {puzzle1(raw)}")
print(f"Puzzle 2: {puzzle2(raw)}")