import numpy as np

from aoc import read_input

def sorted_seats(raw):
    m = dict(F='0',B='1',L='0',R='1')
    return sorted([int(''.join(map(lambda c:m[c], seat)), 2) for seat in raw])

def puzzle1(ss):
    return max(ss)

def puzzle2(ss):
    ss = np.array(ss)
    (idx, *_), *_ = np.where(ss[1:]-ss[:-1] == 2)
    return ss[idx] + 1

ss = sorted_seats(read_input(__file__).split())

print("Puzzle 1: {}".format(puzzle1(ss)))
print("Puzzle 2: {}".format(puzzle2(ss)))
