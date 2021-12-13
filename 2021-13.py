#!/usr/bin/env python3

import re

import matplotlib.pyplot as plt

from aoc import read_input

def do_folds(dots, folds):
    dots = set(dots)
    for ori, pos in folds:
        fold = set()
        for dx, dy in dots:
            if ori == "x":
                if dx > pos:
                    fold |= {(2*pos-dx, dy)}
                else:
                    fold |= {(dx, dy)}
            else:
                if dy > pos:
                    fold |= {(dx, 2*pos-dy)}
                else:
                    fold |= {(dx, dy)}
        dots = fold
    return dots
        

def puzzle1(dots, folds):
    return len(do_folds(dots, folds[:1]))

def puzzle2(dots, folds):
    dots = do_folds(dots, folds)
    plt.scatter([x for x, _ in dots], [-y for _, y in dots])
    plt.gca().set_aspect('equal', adjustable='box')    
    plt.show()
    return "See plot ..."

raw = read_input(2021, 13)
dots, folds = raw.split("\n\n")
dots = [(int(x), int(y)) for x, y in (l.split(",") for l in dots.split())]
folds = list(map(lambda l: (l[0], int(l[1])), re.findall("fold along (.)=(\d+)\n", folds)))

print(f"\033[97m★\033[00m {puzzle1(dots, folds)}")
print(f"\033[93m★\033[00m {puzzle2(dots, folds)}")