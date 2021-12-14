#!/usr/bin/env python3

from collections import defaultdict
import re

from aoc import read_input

def synthesize(start, subs, rounds):
    start = "#" + start + "#"
    counts = defaultdict(int)
    for e1, e2 in zip(start, start[1:]):
        counts[e1 + e2] += 1
    
    for _ in range(rounds):
        counts_new = defaultdict(int)
        for (e1, e2), e3 in subs.items():
            counts_new[e1 + e3] += counts[e1 + e2]
            counts_new[e3 + e2] += counts[e1 + e2]
        counts = counts_new
    
    count = defaultdict(int)
    for e1, e2 in counts:
        count[e1] += counts[e1 + e2]
        count[e2] += counts[e1 + e2]
    
    least, *_, most = sorted([count[e]//2 for e in count if e.isalpha()])
    return most - least

raw = read_input(2021, 14)
start, subs = raw.split('\n\n')
subs = dict(re.findall("(\w+) -> (\w)+", subs))

print(f"\033[97m★\033[00m {synthesize(start, subs, 10)}")
print(f"\033[93m★\033[00m {synthesize(start, subs, 40)}")