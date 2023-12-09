#!/usr/bin/env python3

from tools import *

def interp(hist):
    if not any(hist):
        return (0, 0)
    (*head, _), (_, *tail) = hist, hist
    deriv = list( b-a for a, b in zip(head, tail))
    front, back = interp(deriv)
    return hist[0] - front, hist[-1] + back

def puzzle1(values):
    return sum(back for _, back in values)

def puzzle2(values):
    return sum(front for front, _ in values)

raw = read_input(2023, 9, 'bb')
hists = blist(map(ints, raw.splitlines()))
values = hists >> interp

print(f"\033[97m★\033[00m {puzzle1(values)}")
print(f"\033[93m★\033[00m {puzzle2(values)}")