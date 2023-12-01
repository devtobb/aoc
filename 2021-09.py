#!/usr/bin/env python3

from math import prod

import numpy as np
from scipy.ndimage.measurements import label

from aoc import read_input

def puzzle1(a):
    ap = np.pad(a, 1, mode='constant', constant_values=10)
    mini = ((a < ap[:-2, 1:-1]) & 
            (a < ap[2:, 1:-1]) & 
            (a < ap[1:-1, :-2]) & 
            (a < ap[1:-1, 2:]))
    return sum(a[mini] + 1)


def puzzle2(a):
    c, n = label(a<9, structure=[[0,1,0],[1,0,1],[0,1,0]])
    _, s = np.unique(c, return_counts=True)
    return prod(sorted(s)[-4:-1])

a = np.array(list(map(list, read_input(2021, 9).split())), dtype=int)

print(f"Puzzle 1: {puzzle1(a)}")
print(f"Puzzle 2: {puzzle2(a)}")
