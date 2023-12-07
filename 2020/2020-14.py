#!/usr/bin/env python3

import re

from tools import read_input

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
    masks  = []
    mem = {}
    for i in instr:
        if i['mask']:
            n = i['mask'].count('X')
            mask_1 = int(i['mask'].translate({88:49}), 2)
            repl = [ list(("{:0"+str(n)+"b}").format(m)) for m in range(2**n)] 
            mask_template = i['mask'].translate({88:'{}', 48:49})
            masks = [ int(mask_template.format(*r), 2) for r in repl]
        else:
            for mask in masks:
                addr = (int(i['addr']) | mask_1) & mask
                mem[addr] = int(i['value'])

    return sum(mem.values())


r = r"(mask = (?P<mask>[10X]+))|(mem\[(?P<addr>\d+)\] = (?P<value>\d+))"
raw = read_input(2020, 14).split('\n')[:-1]
instr = [re.match(r, row).groupdict() for row in raw]

print("Puzzle 1: {}".format(puzzle1(instr)))
print("Puzzle 2: {}".format(puzzle2()))