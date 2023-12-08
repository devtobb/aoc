#!/usr/bin/env python3

from itertools import cycle
from math import lcm

from tools import read_input

def n_steps(pos, stop):
    for n, i in enumerate(cycle(instr), 1):
        pos = nodes[pos][i]
        if stop(pos):
            return n

def puzzle1():
    return n_steps('AAA', lambda p: p=='ZZZ')

def puzzle2():
    starts = [pos for pos in nodes.keys() if pos.endswith('A')]
    steps = [n_steps(p, lambda p: p.endswith('Z')) for p in starts]
    return lcm(*steps)

raw = read_input(2023, 8)
instr, nodes = raw.split('\n\n')
nodes = {l[0:3]:dict(L=l[7:10], R=l[12:15]) for l in nodes.splitlines()}

print(f"\033[97m★\033[00m {puzzle1()}")
print(f"\033[93m★\033[00m {puzzle2()}")