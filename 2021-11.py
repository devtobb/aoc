#!/usr/bin/env python3

import numpy as np

from itertools import product

from aoc import read_input


def solve(octo):
    wy, wx = octo.shape
    flashes = 0
    can_flash = np.ones(octo.shape)
    n_flashes_100 = 0 
    n = 0
    while np.any(can_flash):
        octo += 1
        n += 1
        can_flash = np.ones(octo.shape)
        flashed = True
        while flashed:
            flashed = False
            for y, x in zip(*np.where(octo>9)):
                if can_flash[y, x]:
                    can_flash[y, x] = False
                    flashed = True
                    flashes += 1
                    for cy, cx in product(range(y-1, y+2), range(x-1, x+2)):
                        if cy>=0 and cy<wy and cx>=0 and cx<wx and (cy!=y or cx!=x):
                            octo[cy, cx] += 1
        octo[np.logical_not(can_flash)]=0
        if n==100:
            n_flashes_100 = flashes

    return n_flashes_100, n

def puzzle2():
    pass

raw = read_input(2021, 11)
octo = np.array(list(map(list, raw.split())), dtype=int) 
p1, p2 = solve(octo)

print(f"Puzzle 1: {p1}")
print(f"Puzzle 2: {p2}")