#!/usr/bin/env python3

import re

import matplotlib.pyplot as plt

from aoc import read_input

def fold_coord(coord, pos):
    return 2*pos-coord if coord>pos else coord

def do_folds(dots, folds):
    dots = set(dots)
    for ori, pos in folds:
        f = dict(
            x=lambda p: (fold_coord(p[0], pos), p[1]),
            y=lambda p: (p[0], fold_coord(p[1], pos))
        )
        dots = set(map(f[ori], dots))
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