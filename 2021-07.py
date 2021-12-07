#!/usr/bin/env python3
from statistics import median

from aoc import read_input

def puzzle1(crabs):
    opt = median(crabs)
    return int(sum((abs(opt-c) for c in crabs)))

def puzzle2(crabs):
    opt = sum(crabs)//len(crabs)
    return sum(((abs(c-opt)*(abs(c-opt)+1)) // 2) for c in crabs)

raw = read_input(2021, 7)
crabs = list(map(int, raw.split(",")))

print(f"Puzzle 1: {puzzle1(crabs)}")
print(f"Puzzle 2: {puzzle2(crabs)}")