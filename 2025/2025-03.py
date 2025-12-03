#!/usr/bin/env python3

from tools import *

def max_joltage(row, max_bats=2):
    mx = []
    for n in range(max_bats):
        mx.append(max(row[:len(row) - (max_bats - n - 1)]))
        row = row[row.index(mx[n])+1:]
    return int("".join(mx))

def puzzle1(bats):
    return sum(map(max_joltage, bats))

def puzzle2(bats):
    return sum(map(lambda row:max_joltage(row, 12), bats))

raw = read_input(2025, 3)
bats = list(map(list, raw.split()))

print(f"\033[97m★\033[00m {puzzle1(bats)}")
print(f"\033[93m★\033[00m {puzzle2(bats)}")