#!/usr/bin/env python3

from collections import namedtuple

P = namedtuple('P', 'row col')

P.__add__ = lambda self, other: P(self.row+other.row, self.col+other.col)

from tools import *

lookup = {
    '-': {
        P(1, 0) : [P(0, 1), P(0, -1)],
        P(-1, 0) : [P(0, 1), P(0, -1)],
        P(0, 1) : [P(0, 1)],
        P(0, -1): [P(0, -1)],
    },
    '|' : {
        P(0, 1) : [P(1, 0), P(-1, 0)],
        P(0, -1) : [P(1, 0), P(-1, 0)],
        P(1, 0) : [P(1, 0)],
        P(-1, 0) : [P(-1, 0)]
    },
    '\\' : {
        P(1, 0) : [P(0, 1)],
        P(-1, 0) : [P(0, -1)],
        P(0, 1) : [P(1, 0)],
        P(0, -1) : [P(-1, 0)],
    },
    '/' : {
        P(1, 0) : [P(0, -1)],
        P(-1, 0) : [P(0, 1)],
        P(0, 1) : [P(-1, 0)],
        P(0, -1) : [P(1, 0)],
    },
    '.' : {
        P(1, 0) : [P(1, 0)],
        P(-1, 0): [P(-1, 0)],
        P(0, 1) : [P(0, 1)],
        P(0, -1) : [P(0, -1)]
    }
}


def run(grid, start):
    height = len(grid)
    width = len(grid[0])
    
    def on_grid(pos: P):
        return pos.row in range(height) and pos.col in range(width)

    queue = [start]
    energ = set()
    visited = set()

    while queue:
        pos, d = queue.pop()
        # print(pos, d)
        if on_grid(pos):
            energ.add(pos)
            for new_d in lookup[grid[pos.row][pos.col]][d]:
                if (pos+new_d, new_d) not in visited:
                    queue.append((pos+new_d, new_d))
                    visited.add((pos+new_d, new_d))

    return len(energ)

def puzzle1(grid):
    return run(grid, (P(0, 0), P(0, 1)))

def puzzle2(grid):
    height = len(grid)
    width = len(grid[0])
    mx = 0
    for row in range(height):
        for col in range(width):
            for d in (P(1, 0), P(-1,0), P(0,1), P(0,-1)):
                mx = max(mx, run(grid, (P(row, col), d)))

        print(f"done row {row}")
    return mx


raw = read_input(2023, 16)
grid = raw.splitlines()


print(f"\033[97m★\033[00m {puzzle1(grid)}")
print(f"\033[93m★\033[00m {puzzle2(grid)}")