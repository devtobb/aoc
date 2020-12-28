#!/usr/bin/env python3

from collections import defaultdict

from aoc import read_input

def instr_str_to_int(instr):
    repl = [('nw','1'),('ne','2'),('se','4'),('sw','5'),('w','0'),('e','3')]
    for r, s in repl:
        instr = instr.replace(r, s)

    return list(map(int, list(instr)))

def instr_to_tile(instr):
    directions = [1, 1-1j, -1j, -1, -1+1j, 1j]

    return sum(directions[n] for n in instr)

def puzzle1(instr):
    tiles = defaultdict(lambda: False)
    for i in instr:
        tile = instr_to_tile(i)
        tiles[tile] = not tiles[tile]

    return sum(tiles.values())

def puzzle2():
    pass

raw = read_input(2020, 24).split()
instr = list(map(instr_str_to_int, raw))


print(f"Puzzle 1: {puzzle1(instr)}")
print(f"Puzzle 2: {puzzle2()}")