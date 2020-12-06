#!/usr/bin/env python3

from aoc import read_input

def fuel_required(mass):
    fuel = mass//3-2
    if fuel <= 0:
        return 0
    else:
        return fuel + fuel_required(fuel)

def mass_to_fuel(masses):
    return map(lambda m: m//3-2 if m//3-2>=0 else 0, masses)

def puzzle1(masses):
    return sum(mass_to_fuel(masses))

def puzzle2(masses):
    return sum(map(fuel_required, masses))

masses = list(map(int, read_input(2019, 1).split()))

print("Puzzle 1: {}".format(puzzle1(masses)))
print("Puzzle 2: {}".format(puzzle2(masses)))