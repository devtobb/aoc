#!/usr/bin/env python3

from itertools import permutations

from tools import read_input

def puzzle1(raw):
    total = 0
    for _, signals in raw:
        total += len(list(filter(lambda n: n in (2,3,4,7), map(len, signals))))
    return total

def puzzle2(raw):
    digits = 'abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg'.split()
    total = 0
    for patterns, signals in raw:
        for p in permutations("abcdefg"):
            trans = {ord(i):o for (i,o) in zip(list("abcdefg"), p)}
            if all(''.join(sorted(pat.translate(trans))) in digits for pat in patterns):
                res = [digits.index(''.join(sorted(s.translate(trans)))) for s in signals]
                total += int(''.join(map(str, res)))
    return total

raw = read_input(2021, 8)
raw =  [list(map(str.split, l.split(' | '))) for l in raw.split('\n')[:-1]]

print(f"Puzzle 1: {puzzle1(raw)}")
print(f"Puzzle 2: {puzzle2(raw)}")