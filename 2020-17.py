#!/usr/bin/env python3

from itertools import product

import numpy as np

from aoc import read_input

def step(grid):
    new_grid = np.zeros(grid.shape)
    height, width, depth = grid.shape
    for y, x, z in product(*(range(n) for n in grid.shape)):
        sum_ = np.sum(grid[max(0,y-1):min(height,y+2), max(0,x-1):min(width,x+2), max(0,z-1):min(depth,z+2)])
        sum_ -= grid[y, x, z]
        new_grid[y, x, z] = (
            (grid[y, x, z] and 2 <= sum_ <= 3) or
            (not grid[y, x, z] and sum_ == 3)
        )
    return new_grid


def trim3d(arr):
    xs, ys, zs = np.where(arr!=0)
    return arr[min(xs):max(xs)+1, min(ys):max(ys)+1, min(zs):max(zs)+1]

def print_grid(grid):
    np.set_printoptions(threshold=9223372036854775807)
    grid = trim3d(grid)
    _, _, depth = grid.shape
    for d in range(depth):
        print("-"*10, d)
        print(grid[:, :, d])

def puzzle1(start_grid, max_iter):
    height, width = start_grid.shape
    grid = np.zeros((height+2*max_iter, width+2*6*max_iter, 2*max_iter+1))
    grid[max_iter:max_iter+height, max_iter:max_iter+width, 6] = start_grid

    # print_grid(grid)
    for _ in range(max_iter):
        # print('#'*80)
        # print(n)
        # print('#'*80)
        grid = step(grid)
        # print_grid(grid[3:8+2*3, 3:8+2*3, 3:8+2*3])
        # print_grid(grid)

    return np.sum(grid)

def puzzle2():
    pass

raw = read_input(2020, 17)
start_grid = np.fromstring(raw.translate({35:'1 ',46:'0 '}), sep=' ')
start_grid.shape = raw.count('\n'), raw.count('\n')

print(f"Puzzle 1: {puzzle1(start_grid, 6)}")
print(f"Puzzle 2: {puzzle2()}")