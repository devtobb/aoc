#!/usr/bin/env python3

from itertools import product

from tools import *

class Grid:
    def __init__(self, lines):
        self.lines = [list(line) for line in lines]

    def is_row_empty(self, row):
        return all(f=='.' for f in self.lines[row])

    def is_col_empty(self, col):
        return all(line[col] == '.' for line in self.lines)

    def insert_row(self, row):
        self.lines.insert(row, ['.'] * self.width)

    def insert_col(self, col):
        for line in self.lines:
            line.insert(col, '.')
    
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
    empty_rows = [ n for n in range(grid.height) if grid.is_row_empty(n)]
    empty_cols = [ n for n in range(grid.width) if grid.is_col_empty(n)]

    for row in reversed(empty_rows):
        grid.insert_row(row)

    for col in reversed(empty_cols):
        grid.insert_col(col)

    return sum( abs(ar-br)+abs(ac-bc) for (ar, ac), (br, bc) in product(grid.galaxies, grid.galaxies) ) // 2

def puzzle2():
    pass

raw = read_input(2023, 11)
grid = Grid(raw.splitlines())


print(f"\033[97m★\033[00m {puzzle1(grid)}")
print(f"\033[93m★\033[00m {puzzle2()}")