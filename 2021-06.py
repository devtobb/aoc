#!/usr/bin/env python3

from aoc import read_input

def run_days(fish, days):
    n_fish = [fish.count(d) for d in range(9)]
    zero = 0
    for d in range(days):
        zero = (zero + 1) % 9
        n_fish[(zero + 6) % 9] += n_fish[(zero + 8) % 9]

    return sum(n_fish)

def puzzle1(fish):
    return run_days(fish, 80)

def puzzle2(fish):
    return run_days(fish, 256)

raw = read_input(2021, 6)
fish = list(map(int, raw.split(','))) 

print(f"Puzzle 1: {puzzle1(fish)}")
print(f"Puzzle 2: {puzzle2(fish)}")