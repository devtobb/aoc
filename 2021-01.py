#!/usr/bin/env python3
import numpy as np

from aoc import read_input

def puzzle1(raw):
    return sum((raw[1:] - raw[:-1]) > 0 )

def puzzle2(raw):
    wdw = raw[:-2] + raw[1:-1] + raw[2:]
    return sum((wdw[1:] - wdw[:-1]) > 0 )

raw = np.array(list(map(int, read_input(2021, 1).split())))

print(f"Puzzle 1: {puzzle1(raw)}")
print(f"Puzzle 2: {puzzle2(raw)}")