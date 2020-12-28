#!/usr/bin/env python3

from collections import defaultdict

from aoc import read_input

repl = [('nw','1'),('ne','2'),('se','4'),('sw','5'),('w','0'),('e','3')]
neighbors = [1, 1-1j, -1j, -1, -1+1j, 1j]

def instr_str_to_int(instr):
    for r, s in repl:
        instr = instr.replace(r, s)

    return list(map(int, list(instr)))

def instr_to_tile(instr):
    return sum(neighbors[n] for n in instr)

def tiles_from_instr(instr):
    tiles = defaultdict(lambda: False)
    for i in instr:
        tile = instr_to_tile(i)
        tiles[tile] = not tiles[tile]

    return tiles

def trim_tiles(tiles):
    return defaultdict(lambda: False, {tile:True for tile in tiles if tiles[tile]})

def puzzle1(tiles):
    return sum(tiles.values())

def puzzle2(tiles):
    for _ in range(100):
        tiles_new = defaultdict(lambda: False)
        for tile in list(tiles):
            for neigh in neighbors:
                if tile + neigh not in tiles_new:
                    neigh_black = sum(tiles[tile + neigh + d] for d in neighbors)
                    tiles_new[tile + neigh] = ((tiles[tile + neigh] and neigh_black in (1, 2)) or
                                                not tiles[tile + neigh] and neigh_black == 2)

        tiles = trim_tiles(tiles_new)

    return sum(tiles.values())

raw = read_input(2020, 24).split()
instr = list(map(instr_str_to_int, raw))
tiles = tiles_from_instr(instr)

print(f"Puzzle 1: {puzzle1(tiles)}")
print(f"Puzzle 2: {puzzle2(tiles)}")