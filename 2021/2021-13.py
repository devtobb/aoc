#!/usr/bin/env python3

import re

import matplotlib.pyplot as plt

from tools import read_input

def do_folds(dots, folds):
    for ori, pos in folds:
        f = dict(
            x=lambda p: (min(2*pos-p[0], p[0]), p[1]),
            y=lambda p: (p[0], min(2*pos-p[1], p[1]))
        )
        dots = set(map(f[ori], dots))
    return dots

def puzzle1(dots, folds):
    return len(do_folds(dots, folds[:1]))

def puzzle2(dots, folds):
    dots = do_folds(dots, folds)
    plt.scatter([x for x, _ in dots], [-y for _, y in dots])
    plt.gca().set_aspect(1)    
    plt.show()
    return "See plot ..."

raw = read_input(2021, 13)
dots = {tuple(map(int, c)) for c in re.findall("(\d+),(\d+)", raw)}
folds = [(o, int(p)) for o, p in re.findall("(.)=(\d+)", raw)]

print(f"\033[97m★\033[00m {puzzle1(dots, folds)}")
print(f"\033[93m★\033[00m {puzzle2(dots, folds)}")