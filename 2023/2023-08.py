#!/usr/bin/env python3

from itertools import cycle
from functools import reduce
from math import lcm

from tools import read_input

def n_steps(start, nodes, instr, stop):
    for n, i in enumerate(cycle(instr), 1):
        start = nodes[start][i]
        if stop(start):
            return n

def puzzle1(nodes, instr):
    return n_steps('AAA', nodes, instr, lambda p: p=='ZZZ')

def puzzle2(nodes, instr):
    return lcm(*(n_steps(start, nodes, instr, lambda p: p.endswith('Z')) for start in nodes.keys() if start.endswith('A')))


raw = read_input(2023, 8)
instr, nodes = raw.split('\n\n')
instr = list(instr)
nodes = nodes.splitlines()
nodes = {l[0:3]:dict(L=l[7:10], R=l[12:15]) for l in nodes}

print(f"\033[97m★\033[00m {puzzle1(nodes, instr)}")
print(f"\033[93m★\033[00m {puzzle2(nodes, instr)}")