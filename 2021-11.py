#!/usr/bin/env python3

import numpy as np

from itertools import product

from aoc import read_input


def solve(octo):
    octo = np.pad(octo, 1, mode='constant', constant_values=0)
    core = np.s_[1:-1, 1:-1]
    neigh = np.array([[1,1,1],[1,0,1],[1,1,1]], dtype=np.ubyte)
    flashes = 0
    n = 0
    
    can_flash = np.ones(octo[core].shape)
    while np.any(can_flash):
        octo += 1
        n += 1
        can_flash = np.ones(octo[core].shape)
        
        flashed = True
        while flashed:
            flashed = False
            for y, x in zip(*np.where(octo[core]>9)):
                if can_flash[y, x]:
                    can_flash[y, x] = False
                    flashed = True
                    if n<=100: flashes += 1
                    octo[y:y+3,x:x+3] += neigh
        
        octo[core][np.logical_not(can_flash)]=0

    return flashes, n

def puzzle2():
    pass

raw = read_input(2021, 11)
octo = np.array(list(map(list, raw.split())), dtype=np.ubyte) 
p1, p2 = solve(octo)

print(f"Puzzle 1: {p1}")
print(f"Puzzle 2: {p2}")