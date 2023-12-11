#!/usr/bin/env python3

from functools import cache
from itertools import combinations

from tools import *

class Grid:
    def __init__(self, lines):
        self.lines = [list(line) for line in lines]

    @cache
    def is_row_empty(self, row):
        return all(f=='.' for f in self.lines[row])

    @cache
    def is_col_empty(self, col):
        return all(line[col] == '.' for line in self.lines)
   
    def dist(self, a, b, empty_adds=1):
        ar, ac = a
        br, bc = b
        ar, br = min(ar, br), max(ar, br)
        ac, bc = min(ac, bc), max(ac, bc)
        empty_rows = sum(self.is_row_empty(row) for row in range(ar+1, br))
        empty_cols = sum(self.is_col_empty(col) for col in range(ac+1, bc))
        return (br-ar) + (bc-ac) + empty_rows*empty_adds + empty_cols*empty_adds

    @property
    def galaxies(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.lines[row][col] == '#':
                    yield (row, col)

    @property
    def width(self):
        return len(self.lines[0])

    @property
    def height(self):
        return len(self.lines)

    def __str__(self):
        return '\n'.join(''.join(line) for line in self.lines)

def puzzle1(grid: Grid):
    return sum( grid.dist(a, b) for a, b in combinations(grid.galaxies, 2) )

def puzzle2():
    return sum( grid.dist(a, b, empty_adds=999_999) for a, b in combinations(grid.galaxies, 2) )


raw = read_input(2023, 11)
grid = Grid(raw.splitlines())


print(f"\033[97m★\033[00m {puzzle1(grid)}")
print(f"\033[93m★\033[00m {puzzle2()}")