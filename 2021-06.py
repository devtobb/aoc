#!/usr/bin/env python3

from aoc import read_input

def run_days(n_fish, days):
    for d in range(days):
        n_fish[(d + 7) % 9] += n_fish[d % 9]

    return sum(n_fish)

def puzzle1(n_fish):
    return run_days(n_fish, 80)

def puzzle2(n_fish):
    return run_days(n_fish, 256)

raw = read_input(2021, 6)
fish = list(map(int, raw.split(','))) 
n_fish = [fish.count(d) for d in range(9)]

print(f"Puzzle 1: {puzzle1(n_fish.copy())}")
print(f"Puzzle 2: {puzzle2(n_fish.copy())}")