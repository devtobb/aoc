#!/usr/bin/env python3

from aoc import read_input

def run_days(fish, days):
    n_fish = {d:fish.count(d) for d in range(9)}
    for d in range(days):
        n_fish = {n:n_fish[(n+1)%9] for n in range(9)}
        n_fish[6] += n_fish[8]

    return sum((n for n in n_fish.values()))

def puzzle1(fish):
    return run_days(fish, 80)

def puzzle2(fish):
    return run_days(fish, 256)

raw = read_input(2021, 6)
fish = list(map(int, raw.split(','))) 

print(f"Puzzle 1: {puzzle1(fish)}")
print(f"Puzzle 2: {puzzle2(fish)}")