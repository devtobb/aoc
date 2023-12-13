#!/usr/bin/env python3

from tools import *

def horsplit(pattern):
    height = len(pattern)
    for row in range(1, height):
        upper = reversed(pattern[:row])
        lower = pattern[row:]

        eq = True
        for l1, l2 in zip(upper, lower):
            if l1!=l2:
                eq = False
                break
        if eq:
            return row
    
    return 0

def transpose(pattern):
    return [''.join(l) for l in zip(*pattern)]


def vertsplit(pattern):
    return horsplit(transpose(pattern))

def puzzle1(patterns):
    return (
        sum(map(vertsplit, patterns)) + 
        100 * sum(map(horsplit, patterns))
    )

def puzzle2():
    pass


raw = read_input(2023, 13, '')
patterns = raw.split('\n\n')
patterns = [pattern.splitlines() for pattern in patterns]



print(f"\033[97m★\033[00m {puzzle1(patterns)}")
print(f"\033[93m★\033[00m {puzzle2()}")