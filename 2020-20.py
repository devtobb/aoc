#!/usr/bin/env python3


from itertools import product
import numpy as np
from math import prod
from copy import deepcopy

from aoc import read_input

class Tile():

    def __init__(self, number, tile):
        self.rotation = 0
        self.flip = False
        self.number = number
        self.tile = np.array(tile)
        self.neighbors = []
        self.calculate_borders()
        self.aligned = False

    def calculate_borders(self):
        self.borders=[]
        for b in (                          
                    self.tile[:, -1],       # 0 east
                    self.tile[0, :],        # 1 north
                    self.tile[:, 0],        # 2 west
                    self.tile[-1, :],       # 3 south
                    self.tile[::-1, -1],    # 4 east_flipped
                    self.tile[0, ::-1],     # 5 north_flipped
                    self.tile[::-1, 0],     # 6 west_flipped
                    self.tile[-1, ::-1],    # 7 south_flipped
                ):
            self.borders.append(int(''.join(str(n) for n in b), 2))

    def add_neighbor(self, other):
        if self.number != other.number:
            if any(a==b for (a, b) in product(self.borders, other.borders)):
                self.neighbors.append(other.number)

    def neigh_pos(self, tile_dict):
        borders = self.borders[ 4 * self.flip: 4 * (self.flip + 1)]
        pos = []
        for neigh in self.get_neighbors(tile_dict):
            for (n, b) in enumerate(borders):
                if b in neigh.borders:
                    pos.append(n)
        return pos
        # return [n for (n, b) in enumerate(borders) for neigh in self.get_neighbors(tile_dict) for bo in neigh.borders if b==bo]
        
    def neigh_flip(self, tile_dict):
        borders = self.borders[ 4 * self.flip: 4 * (self.flip + 1)]
        flips = []
        for neigh in self.get_neighbors(tile_dict):
            for (n, bo) in enumerate(neigh.borders):
                if bo in borders:
                    flips.append(n>3)
        return flips

    def self_from_neighbors(self, tile_dict):
        borders = self.borders[ 4 * self.flip: 4 * (self.flip + 1)]
        print(borders)
        pos = []
        for neigh in self.get_neighbors(tile_dict):
            print(neigh.borders)
            for (n, bo) in enumerate(neigh.borders):
                if bo in borders:
                    pos.append(n%4)    
        return pos

    def align_neighbors(self, tile_dict):
        flips = self.neigh_flip(tile_dict)
        rots = self.neigh_rot(tile_dict)
        # print(f"Starting align: {flips} {rots}")
        for neigh, flip, rot in zip(self.get_neighbors(tile_dict), flips, rots):
            # print(f"Checking: {neigh}")
            if not neigh.aligned:
                # print(f"Not yet aligned: {neigh}")
                neigh.aligned = True
                neigh.flip = flip
                neigh.rotation = rot
                # neigh.align_neighbors(tile_dict)
            else:
                if not(neigh.flip==flip and neigh.rotation==rot):
                    print(f"!!!!!!!!!!!!!!!!!not matching {neigh}")
                #     raise Exception("FUUUUUUUUUUU")

    def neigh_rot(self, tile_dict):
        r = []
        for f, fi in zip(self.neigh_pos(tile_dict), self.self_from_neighbors(tile_dict)):
            print(f, fi)
            r.append((fi - (f+self.rotation+2)%4)%4)
        return r

    def get_neighbors(self, tile_dict):
        return [tile_dict[tile] for tile in self.neighbors]

    def __repr__(self):
        return f"{self.number}: Borders: {self.borders} Neigh: {self.neighbors}"

    def __str__(self):
        return self.__repr__()
    
    def __getitem__(self, key):
        print(key)


def tile_to_bin(tile):
    tile = [list(row.translate({35:'1',46:'0',32:'0'})) for row in tile]
    return [[int(cell) for cell in row] for row in tile]

def puzzle1(tiles):
    for tile in tiles:
        for other in tiles:
            tile.add_neighbor(other)
    
    return prod(tile.number for tile in tiles if len(tile.neighbors)==2)

def puzzle2():
    pass

raw = read_input(2020, 20)
tiles = [Tile(int(num[5:]), tile_to_bin(img.split())) for (num, img) in (tile.split(':') for tile in raw.split('\n\n')[:-1])]
tile_dict = {tile.number:tile for tile in tiles}

print(f"Puzzle 1: {puzzle1(tiles)}")

grid = [[None]*12 for _ in range(12)]

tiles = sorted(tiles, key=lambda t: len(t.neighbors))
first, *_ = tiles

first.tile = np.rot90(first.tile, 2)
grid[0][0] = first.number
used = []
for y, x in product(range(12), range(12)):
    # print(f"y{y} x{x}")
    if y==0 and x==0:
        continue
    
    found = False
    
    if y > 0:
        ref = tile_dict[grid[y-1][x]]
        left = True
    else:
        ref = tile_dict[grid[y][x-1]]
        left = False
    
    for neigh in ref.get_neighbors(tile_dict):
        # print(f"checking {neigh}")
        if found:
            break
    
        for rot, flip in product(range(4), (1, -1)):
            # print(f"checking rot: {rot} flip: {flip}")
            arr = np.rot90(neigh.tile, rot)[:, ::flip]
            if (all(ref.tile[:, -1] == arr[:, 0]) and not left) or (all(ref.tile[-1] == arr[0]) and left):
                neigh.tile = arr
                found = True
                used.append(neigh.number)
                grid[y][x] = neigh.number
                break
    if not found:
        print(f"No neigh for {ref}")
        raise Exception("FUUUUUUU")

picture = np.zeros((96, 96))
for y, x in product(range(12), range(12)):
    # print(f"copying {y}, {x}")
    picture[y*8:(y+1)*8, x*8:(x+1)*8] = tile_dict[grid[y][x]].tile[1:-1, 1:-1]

monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
monster = np.array(tile_to_bin(monster.split('\n')[1:-1]))

test_field ="""
.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###
"""

test_field = np.array(tile_to_bin(test_field.split('\n')[1:-1])) 
# picture = test_field
roughness = []
ft = []
not_monster = np.ones(picture.shape)

print(picture)
print(not_monster)

found = False
for rot, flip in product(range(4), (1, -1)):
    print(f"checking [r={rot}, f={flip}]")
    pic = np.rot90(picture, rot)[:, ::flip]
    not_monster = np.rot90(not_monster, rot)[:, ::flip]
    print(picture)
    print(not_monster)
    for y, x in product(range(94), range(77)):
    # for y, x in product(range(22), range(5)):
        if np.sum(np.logical_and(pic[y:y+3, x:x+20], monster)) == 15:
            found = True
            # ron = np.sum(np.logical_and(pic[y:y+3, x:x+20], np.logical_not(monster)))
            # ft.append(pic[y:y+3, x:x+20])
            print(f"Monster at ({y}, {x}) -- [r={rot}, f={flip}]")
            not_monster[y:y+3, x:x+20] = np.logical_and(not_monster[y:y+3, x:x+20], np.logical_not(monster))
    if found:
        break
# # not generally true:
# first.rotation = max(first_neigh_pos) if max(first_neigh_pos) != 3 else 0
# first.aligned = True

# fullpic = np.zeros((120, 120))
# for y, x in product(range(12), range(12)):
#     fullpic[y*10:(y+1)*10, x*10:(x+1)*10] = tile_dict[grid[y][x]].tile

    # fullpic[y*10:(y+1)*10, x*10+1] += 5 * tile_dict[grid[y][x]].tile[:, 0]

print(f"Puzzle 2: {np.sum(np.logical_and(not_monster, pic))}")