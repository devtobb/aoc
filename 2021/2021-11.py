#!/usr/bin/env python3

from itertools import product

import numpy as np

from tools import read_input


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
        
        candidates = [True],
        while len(candidates[0])>0:
            candidates = np.where(np.logical_and(can_flash, octo[core]>9))
            can_flash[candidates] = False
            if n<=100: flashes += len(candidates[0])
            for y, x in zip(*candidates):
                octo[y:y+3,x:x+3] += neigh
        
        octo[core][np.logical_not(can_flash)] = 0

    return flashes, n

raw = read_input(2021, 11)
octo = np.array(list(map(list, raw.split())), dtype=np.ubyte) 
p1, p2 = solve(octo)

print(f"\033[97m★\033[00m {p1}")
print(f"\033[93m★\033[00m {p2}")