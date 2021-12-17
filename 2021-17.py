#!/usr/bin/env python3

import re
from itertools import product

from aoc import read_input

def step(x, y, vx, vy):
    x += vx
    y += vy
    if vx>0: vx-=1
    elif vx<0: vx+=1
    vy -= 1
    return x, y, vx, vy

def all_hits(target, vx_range=range(300), vy_range=range(300)):
    x_min, x_max, y_min, y_max = target
    hits = []
    for sx, sy in product(vx_range, vy_range):
        x, y, vx, vy = 0, 0, sx, sy
        max_height = y
        while x<x_max and y>y_min:
            x, y, vx, vy = step(x, y, vx, vy)
            max_height = max(y, max_height)
            if x>=x_min and x<=x_max and y>=y_min and y<=y_max:
                hits.append((max_height, sx, sy))
                break

    return hits

def puzzle1(target):
    hits = all_hits(target)
    best = sorted(hits, key=lambda x: x[0])
    return best[-1][0]


def puzzle2():
    return len(all_hits(target, vx_range=range(-300, 300), vy_range=range(-300, 300)))

raw = read_input(2021, 17)
target = list(map(int, re.search("x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", raw).groups()))

print(f"\033[97m★\033[00m {puzzle1(target)}")
print(f"\033[93m★\033[00m {puzzle2()}")