#!/usr/bin/env python3

import numpy as np
from scipy.signal import convolve2d

from tools import *

def get_removable(grid):
    (mask:=np.ones((3, 3)))[1, 1]=0
    return np.logical_and(convolve2d(grid, mask, mode='same')<4,  grid)

def puzzle1(grid):
    return int(np.sum(get_removable(grid)))

def puzzle2(grid):
    total_removed = 0
    removed = - 1
    while (removed := np.sum(removable := get_removable(grid))) != 0:
        total_removed += removed
        grid = np.logical_and(grid, np.logical_not(removable))
    return total_removed

raw = read_input(2025, 4)
grid = np.array([[col=="@" for col in row] for row in raw.split()])

print(f"\033[97m★\033[00m {puzzle1(grid)}")
print(f"\033[93m★\033[00m {puzzle2(grid)}")