#!/usr/bin/env python3

import re

from aoc import read_input

def puzzle1(instr):
    mask_0 = int('0'*36, 2)
    mask_1 = int('1'*36, 2)
    mem = dict()
    for i in instr:
        if i['mask']:
            mask_0 = int(i['mask'].translate({88:48}), 2)
            mask_1 = int(i['mask'].translate({88:49}), 2)
        else:
            mem[i['addr']] = (int(i['value']) | mask_0) & mask_1

    return sum(mem.values())

def puzzle2():
    pass

r = r"(mask = (?P<mask>[10X]+))|(mem\[(?P<addr>\d+)\] = (?P<value>\d+))"
raw = read_input(2020, 14).split('\n')[:-1]
instr = [re.match(r, row).groupdict() for row in raw]

print("Puzzle 1: {}".format(puzzle1(instr)))
print("Puzzle 2: {}".format(puzzle2()))