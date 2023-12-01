#!/usr/bin/env python3
from collections import defaultdict
from math import copysign
from itertools import repeat

from aoc import read_input
def lrng(a, b):
    if a==b:
        return repeat(a)
    else:
        sgn = int(copysign(1, b-a))
        return range(a, b+sgn, sgn)

def dangerous(lines):
    field = defaultdict(int)
    for (x1, y1), (x2, y2) in lines:
        for x, y in zip(lrng(x1, x2), lrng(y1, y2)):
            field[(x,y)] += 1

    return sum(( 1 for v in field.values() if v > 1))

def is_not_diag(line):
    (x1, y1), (x2, y2) = line
    return x1==x2 or y1==y2

def puzzle1(lines):
    return dangerous(filter(is_not_diag, lines))

def puzzle2(lines):
    return dangerous(lines)

raw = read_input(2021, 5)
lines = [[list(map(int,p.split(","))) 
            for p in l.split(" -> ")] 
            for l in raw[:-1].split("\n")]

print(f"Puzzle 1: {puzzle1(lines)}")
print(f"Puzzle 2: {puzzle2(lines)}")