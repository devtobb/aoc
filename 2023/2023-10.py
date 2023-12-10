#!/usr/bin/env python3

from math import ceil

from tools import *

def puzzle1():
    pass

def puzzle2():
    pass

raw = read_input(2023, 10)
grid = raw.splitlines()
height, width = len(grid), len(grid[0])
start = raw.index('S')
start = start // (width + 1), start % (width + 1)

direc = dict(N=(-1,0), E=(0,1), S=(1,0), W=(0,-1))
con = {
    '|': (direc['N'], direc['S']),
    '-': (direc['E'], direc['W']),
    'L': (direc['N'], direc['E']),
    'J': (direc['N'], direc['W']),
    '7': (direc['S'], direc['W']),
    'F': (direc['S'], direc['E']),
}

pr, pc = start
cr, cc = pr - 1, pc

steps = 1
while (cr, cc) != start and steps < 1500000:
    for dr, dc in  con[grid[cr][cc]]:
        if (pr, pc) != (cr + dr, cc + dc):
            pr, pc = cr, cc
            cr, cc = (cr + dr, cc + dc)
            break
    steps += 1

print(ceil(steps/2))

# print(f"\033[97m★\033[00m {puzzle1()}")
# print(f"\033[93m★\033[00m {puzzle2()}")