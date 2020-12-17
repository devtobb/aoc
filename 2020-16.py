#!/usr/bin/env python3
import re
import numpy as np
from math import log2, prod

from aoc import read_input

def puzzle1(nearby, valid_lookup):
    return sum(sum(field for field in ticket if not valid_lookup[field]) for ticket in nearby)

def puzzle2(valid, ticket, nearby, valid_lookup):
    nearby = list(filter(lambda t: all(valid_lookup[v] for v in t), nearby))
    m = [2**len(valid)-1]*len(valid)
    for near in nearby:
        for n in range(len(near)):
            m[n] &= valid_lookup[near[n]]
    m = sorted(enumerate(m), key=lambda v: bin(v[1]).count('1'))
    mp = []
    remaining = 2**len(m) - 1
    for idx, mask in m:
        r = remaining & mask
        remaining = remaining - r
        mp.append((idx, int(log2(r))))

    result = []
    for idx, idx2 in mp:
        if valid[idx2][0].startswith("departure"):
            result.append(ticket[idx])
    return prod(result)

raw = read_input(2020, 16)

valid, ticket, nearby = raw.split('\n\n')

re_valid = r'^([^:]+): (\d+)-(\d+) or (\d+)-(\d+)'
valid = [re.match(re_valid, row).groups() for row in valid.split('\n')]
valid_lookup = np.zeros(1000, int)
for n, (_, a1, b1, a2, b2) in enumerate(valid):
    valid_lookup[int(a1):int(b1)+1] += [2**n]*(int(b1) - int (a1) + 1)
    valid_lookup[int(a2):int(b2)+1] += [2**n]*(int(b2) - int (a2) + 1)

_, ticket = ticket.split('\n')
ticket = list(map(int, ticket.split(',')))

_, *nearby, _ = nearby.split('\n')
nearby = [list(map(int, row.split(','))) for row in nearby]

print(f"Puzzle 1: {puzzle1(nearby, valid_lookup)}")
print(f"Puzzle 2: {puzzle2(valid, ticket, nearby, valid_lookup)}")