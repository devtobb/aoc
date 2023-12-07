#!/usr/bin/env python3

from itertools import product

import numpy as np

from tools import read_input

def trim(arr):
    return arr[tuple([slice(min(c), max(c) + 1) for c in np.where(arr)])]

def step(grid):
    grid_new = np.zeros(np.array(grid.shape) + 2, int)

    for coords in product(*(range(n) for n in grid_new.shape)):
        neigh = tuple([slice(max(0,c-2), min(s,c+1)) for c, s in zip(coords, grid.shape)])
        coords_old = tuple(np.array(coords) - 1)

        if all(0<=c<s for c, s in zip(coords_old, grid.shape)):
            value_old = grid[coords_old]
        else:
            value_old = 0
        sum_ = np.sum(grid[neigh]) - value_old
    
        grid_new[coords] = (
            (value_old and 2<=sum_<=3) or
            (not value_old and sum_==3)
        )
        
    return trim(grid_new)

def run(grid, max_iter):
    for _ in range(max_iter):
        grid = step(grid)

    return np.sum(grid)

def puzzle1(start_grid):
    return run(np.array([start_grid]), 6)

def puzzle2(start_grid):
    return run(np.array([[start_grid]]), 6)

raw = read_input(2020, 17)
start_grid = np.fromstring(raw.translate({35:'1 ',46:'0 '}), sep=' ')
start_grid.shape = raw.count('\n'), raw.count('\n')

print(f"Puzzle 1: {puzzle1(start_grid)}")
print(f"Puzzle 2: {puzzle2(start_grid)}")