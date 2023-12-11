#!/usr/bin/env python3

from math import ceil

from tools import *

raw = read_input(2023, 10, '')
grid = [[*line] for line in raw.splitlines()]
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


first_connectors = []
sr, sc = start
for ir, ic in direc.values():
    for dr, dc in con.get(grid[sr+ir][sc+ic], ()):
        if (dr+ir, dc+ic) == (0, 0):
            first_connectors.append((ir, ic))
            pr, pc = start
            cr, cc = sr + ir, sc + ic

print(first_connectors)

a, b = first_connectors
for tile, (d1, d2) in con.items():
    if (d1==a and d2==b) or (d1==b and d2==a):
        if tile == '|':
            grid[sr][sc] = "#"
        elif tile in "7F":
            grid[sr][sc] = "0"
        elif tile in "LJ":
            grid[sr][sc] = "1"
        else:
            grid[sr][sc] = "X"

# if all( r==0 for r, _ in first_connectors):
# else:

# grid[sr][sc] = "0"

steps = 1
while (cr, cc) != start and steps < 1500000:
    for dr, dc in  con[grid[cr][cc]]:
        if (pr, pc) != (cr + dr, cc + dc):
            pr, pc = cr, cc
            cr, cc = (cr + dr, cc + dc)
            if grid[pr][pc] == '|':
                grid[pr][pc] = "#"
            elif grid[pr][pc] in "7F":
                grid[pr][pc] = "0"
            elif grid[pr][pc] in "LJ":
                grid[pr][pc] = "1"
            else:
                grid[pr][pc] = "X"
            break
    steps += 1

puzzle1 = ceil(steps/2)

# F7 -> stay
# FJ -> leave
# L7 -> leave
# LJ -> stay

# 00
# 01
# 10
# 11

puzzle2 = 0
for row in range(height):
    inside = False
    online = False
    lastcorner = ""
    for col in range(width):
        if grid[row][col] == "#":
            inside = not inside 
        else:
            if grid[row][col] in '01':
                if online:
                    inside = inside != (grid[row][col] != lastcorner)
                    online = False
                else:
                    lastcorner = grid[row][col]
                    online = True
            else:
                if grid[row][col] != 'X':
        
                    if inside:
                        puzzle2 += inside
                        grid[row][col] = 'y'
                    assert(grid[row][col] not in "01X#")
    assert not inside and not online, f"{row},{col}"



print("\n".join("".join(line) for line in grid))

print(f"\033[97m★\033[00m {puzzle1}")
print(f"\033[93m★\033[00m {puzzle2}")