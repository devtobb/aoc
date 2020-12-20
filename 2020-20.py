#!/usr/bin/env python3


from itertools import product
import numpy as np
from math import prod
from aoc import read_input

class Tile():

    def __init__(self, number, tile):
        self.rotation = 0
        self.flip = 0
        self.number = number
        self.tile = np.array(tile)
        self.neighbors = []
        self.calculate_borders()

    def calculate_borders(self):
        self.borders=[]
        for b in (
                    self.tile[0, :], 
                    self.tile[-1, :], 
                    self.tile[:, 0], 
                    self.tile[:, -1],
                    self.tile[0, ::-1], 
                    self.tile[-1, ::-1], 
                    self.tile[::-1, 0], 
                    self.tile[::-1, -1],
                ):
            self.borders.append(int(''.join(str(n) for n in b), 2))

    def add_neighbor(self, other):
        if self.number != other.number:
            if any(a==b for (a, b) in product(self.borders, other.borders)):
                self.neighbors.append(other.number)

    def __repr__(self):
        return f"{self.number}: Borders: {self.borders} Neigh: {self.neighbors}"

    def __str__(self):
        return self.__str__()
    
    def __getitem__(self, key):
        print(key)


def tile_to_bin(tile):
    tile = [list(row.translate({35:'1',46:'0'})) for row in tile]
    return [[int(cell) for cell in row] for row in tile]

def puzzle1():
    for tile in tiles:
        for other in tiles:
            tile.add_neighbor(other)
    
    return prod(tile.number for tile in tiles if len(tile.neighbors)==2)

def puzzle2():
    pass

raw = read_input(2020, 20)
tiles = [Tile(int(num[5:]), tile_to_bin(img.split())) for (num, img) in (tile.split(':') for tile in raw.split('\n\n')[:-1])]
    
print(f"Puzzle 1: {puzzle1()}")
print(f"Puzzle 2: {puzzle2()}")