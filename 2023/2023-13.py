#!/usr/bin/env python3

from tools import *

def n_smudges(a, b):
    return sum( ca!=cb for ca, cb in zip(a, b))

def horsplit(pattern, smudges=0):
    height = len(pattern)
    for row in range(1, height):
        upper = reversed(pattern[:row])
        lower = pattern[row:]

        all_smudges = 0
        for a, b in zip(upper, lower):
            all_smudges += n_smudges(a, b)
        if all_smudges==smudges:
            return row
    
    return 0

def transpose(pattern):
    return [''.join(l) for l in zip(*pattern)]

def vertsplit(pattern, smudges=0):
    return horsplit(transpose(pattern), smudges)

def puzzle1(patterns):
    return (
        sum(map(vertsplit, patterns)) + 
        100 * sum(map(horsplit, patterns))
    )

def puzzle2():
    return (
        sum(map(lambda p: vertsplit(p, smudges=1), patterns)) + 
        100 * sum(map(lambda p: horsplit(p, smudges=1), patterns))
    )

raw = read_input(2023, 13, '')
patterns = raw.split('\n\n')
patterns = [pattern.splitlines() for pattern in patterns]

print(f"\033[97m★\033[00m {puzzle1(patterns)}")
print(f"\033[93m★\033[00m {puzzle2()}")