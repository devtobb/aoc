#!/usr/bin/env python3

from math import prod
from aoc import read_input

def puzzle1(departure, busse):
    earliest = min([(bus, bus - departure % bus) for _, bus in busses], key=lambda b: b[1])
    return prod(earliest)

def puzzle2():
    pass

raw = read_input(2020, 13)
departure, busses = raw.split()
departure = int(departure)
busses = [(pos, int(bus)) for pos, bus in enumerate(busses.split(',')) if bus.isdigit()]

print("Puzzle 1: {}".format(puzzle1(departure, busses)))
print("Puzzle 2: {}".format(puzzle2()))