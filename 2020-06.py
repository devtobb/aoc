#!/usr/bin/env python3

from functools import reduce
from operator import and_, or_

from aoc import read_input

def group_reduce(groups, func):
    return sum(len(reduce(func, group)) for group in groups)

def puzzle1(groups):
    return group_reduce(groups, or_)

def puzzle2(groups):
    return group_reduce(groups, and_)

raw = read_input(2020, 6).split('\n\n')
groups = [list(map(set, group.split())) for group in raw]

print("Puzzle 1: {}".format(puzzle1(groups)))
print("Puzzle 2: {}".format(puzzle2(groups)))

