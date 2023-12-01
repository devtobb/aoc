#!/usr/bin/env python3

from collections import deque
from aoc import read_input
from math import prod
from itertools import islice
from functools import cache

def puzzle1(d1, d2):
    d1 = d1.copy()
    d2 = d2.copy()
    while d1 and d2:
        c1, c2 = d1.popleft(), d2.popleft()
        if c1 == c2:
            d1.append(c1)
            d2.append(c2)
        elif c1>c2:
            d1.append(c1)
            d1.append(c2)
        else:
            d2.append(c2)
            d2.append(c1)

    d = d1 if d1 else d2
    d.reverse()
    return sum([(n+1)*c for n,c in  enumerate(d)])

@cache
def rcombat(d1, d2):
    htab = []
    d1 = deque(d1)
    d2 = deque(d2)
    # print(f"recusring: {d1}, {d2}")
    while d1 and d2:
        hsh = hash(d1.__str__() + d2.__str__())
        if hsh in htab:
            return 1, d1
        else:
            htab.append(hsh)

        c1, c2 = d1.popleft(), d2.popleft()
        if len(d1)>=c1 and len(d2)>=c2:
            sub_d1 = tuple(islice(d1, 0, c1))
            sub_d2 = tuple(islice(d2, 0, c2))
            winner, _ = rcombat(sub_d1, sub_d2)
            if winner == 1:
                d1.append(c1)
                d1.append(c2)
            else:
                d2.append(c2)
                d2.append(c1)
        else:
            if c1>c2:
                d1.append(c1)
                d1.append(c2)
            else:
                d2.append(c2)
                d2.append(c1)

    if d1:
        return 1, d1
    else:
        return 2, d2

def puzzle2(d1, d2):
    _, d = rcombat(tuple(d1), tuple(d2))
    d.reverse()
    return sum([(n+1)*c for n,c in  enumerate(d)])


raw = read_input(2020, 22)
d1, d2 = [deque(map(int, row[4:].split())) for row in raw.split('Player')[1:]]

print(f"Puzzle 1: {puzzle1(d1, d2)}")
print(f"Puzzle 2: {puzzle2(d1, d2)}")