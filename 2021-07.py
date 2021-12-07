#!/usr/bin/env python3
from statistics import median, mean
from math import floor, ceil

from aoc import read_input

def solve(crabs, cost, center):
    m = center(crabs)
    opt =  {floor(m), ceil(m)}
    return int(min((sum((cost(c, o) for c in crabs)) for o in opt)))

def puzzle1(crabs):
    cost = lambda crab, pos: abs(crab - pos)
    return solve(crabs, cost, median)

def puzzle2(crabs):
    cost = lambda crab, pos: abs(crab-pos)*(abs(crab-pos)+1)//2
    return solve(crabs, cost, mean)

raw = read_input(2021, 7)
crabs = list(map(int, raw.split(",")))

print(f"Puzzle 1: {puzzle1(crabs)}")
print(f"Puzzle 2: {puzzle2(crabs)}")