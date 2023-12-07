#!/usr/bin/env python3

from functools import reduce

from tools import read_input

class RangeMap(object):
    def __init__(self, line):
        self.dest, self.src, self.length = map(int, line.split())
    
    def __contains__(self, n):
        return n in range(self.src, self.src + self.length)

    def __getitem__(self, n):
        return self.dest + (n - self.src) if n in self else n

    def __str__(self):
        return f"{self.src} -> {self.dest} ({self.length})"
    
    def __repr__(self):
        return f"<Rangemap: {str(self)}>"
        
class Lookup(object):
    def __init__(self, block):
        _, *ranges = block.splitlines()
        self.ranges = tuple(map(RangeMap, ranges))

    def __getitem__(self, n):
        for _range in self.ranges:
            if n in _range : return _range[n]
        return n

    def __str__(self):
        return f"[{','.join(map(str, self.ranges))}]"

    def __repr__(self):
        return f"<Lookup: {str(self)}>"


def puzzle1(lookups, seeds):
    return min(
        reduce(
            lambda value, lookup: lookup[value],
            lookups, 
            seed
        ) for seed in seeds
    )

def puzzle2(lookups, seeds):
    seedrange = zip(seeds[::2], seeds[1::2])
    _min = []
    for start, length in seedrange:
        _min.append(min(
            reduce(
                lambda value, lookup: lookup[value],
                lookups, 
                seed
            ) for seed in range(start, start+length)
            ))
    return min(_min)
    

raw = read_input(2023, 5)
seeds, *blocks = raw.split('\n\n')
_, *seeds = seeds.split()
seeds = tuple(map(int, seeds))
lookups = list(map(Lookup, blocks))

print(f"\033[97m★\033[00m {puzzle1(lookups, seeds)}")
print(f"\033[93m★\033[00m {puzzle2(lookups, seeds)}")