#!/usr/bin/env python3

from tools import *

def interp(hist, sgn, idx):
    if not any(hist):
        return 0
    (*head, _), (_, *tail) = hist, hist
    deriv = list( b-a for a, b in zip(head, tail))
    return sgn*interp(deriv, sgn, idx) + hist[idx]

def puzzle1(hists):
    return sum(hists >> (lambda h: interp(h, 1, -1)))

def puzzle2(hists):
    return sum(hists >> (lambda h: interp(h, -1, 0)))

raw = read_input(2023, 9)
hists = blist(map(ints, raw.splitlines()))

print(f"\033[97m★\033[00m {puzzle1(hists)}")
print(f"\033[93m★\033[00m {puzzle2(hists)}")