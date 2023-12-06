#!/usr/bin/env python3

from math import prod, floor, ceil
from re import findall

from aoc import read_input

def ways_to_win(race):
    time, record = race
    _min, _max = (
        ceil(time/2 - ((time/2)**2 - record)**0.5),
        floor(time/2 + ((time/2)**2 - record)**0.5),
    )
    return _max - _min + 1

def puzzle1(times, records):
    return prod(map(ways_to_win, zip(times, records)))

def puzzle2(times, records):
    race = (
        int(''.join(map(str, times))),
        int(''.join(map(str, records))),
    )
    return ways_to_win(race)

raw = read_input(2023, 6).splitlines()
times, records = (
    tuple(map(int, findall(r'\d+', line))) for line in raw
)

print(f"\033[97m★\033[00m {puzzle1(times, records)}")
print(f"\033[93m★\033[00m {puzzle2(times, records)}")