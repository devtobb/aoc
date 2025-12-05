#!/usr/bin/env python3

from itertools import combinations

from tools import *

def puzzle1(ranges, ids):
    return len(list(filter(lambda i:any(i in r for r in ranges), ids)))

def puzzle2nr(ranges):
    merged = True
    while merged:
        merged = False
        for a, b in combinations(ranges, 2):
            if a.start in b or a.stop-1 in b or b.start in a or b.stop-1 in a:
                ranges.remove(a)
                ranges.remove(b)
                ranges.append(range(min(a.start, b.start), max(a.stop, b.stop)))
                merged = True
                break

    return sum(r.stop - r.start for r in ranges)

raw = read_input(2025, 5)
ranges, ids = raw.split("\n\n")
ranges = [range(int(a), int(b)+1) for a, b in (rng.split("-") for rng in ranges.split())]
ids = list(map(int, ids.split()))

print(f"\033[97m★\033[00m {puzzle1(ranges, ids)}")
print(f"\033[93m★\033[00m {puzzle2nr(ranges)}")