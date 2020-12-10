#!/usr/bin/env python3

import numpy as np

from aoc import read_input

def puzzle1(ad):
    ad = np.array(ad)
    delta = ad[1:] - ad[:-1]
    return sum(delta==1) * sum(delta==3)

def puzzle2(ad):
    incoming = [0]*len(ad)
    for n in range(len(ad)):
        incoming[n] = [i for i in range(max(0, n-3), max(0, n)) if ad[n] - ad[i] <=3]

    pp = [0]*len(incoming)
    pp[0] = 1
    for n in range(1, len(incoming)): 
        pp[n] = sum(pp[i] for i in incoming[n])

    return pp[-1]

raw = read_input(2020, 10)
ad = sorted(list(map(int, raw.split())))
*_, mx = ad
ad = [0] + ad + [mx+3]

print("Puzzle 1: {}".format(puzzle1(ad)))
print("Puzzle 2: {}".format(puzzle2(ad)))
