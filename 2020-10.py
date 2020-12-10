#!/usr/bin/env python3

from aoc import read_input

def puzzle1(adapters):
    delta = [a-b for a, b in zip(adapters[1:], adapters[:-1])] 
    return sum(d==1 for d in delta) * sum(d==3 for d in delta)

def puzzle2(adapters):
    incoming = [[i for i in range(max(0, n-3),  n) if adapters[n] - adapters[i]<=3] for n in range(len(adapters))]
    
    possible_paths = [0]*len(adapters)
    possible_paths[0] = 1
    for n in range(1, len(incoming)): 
        possible_paths[n] = sum(possible_paths[i] for i in incoming[n])

    return possible_paths[-1]

raw = read_input(2020, 10)
adapters = sorted(list(map(int, raw.split())))
*_, maxi = adapters
adapters = [0] + adapters + [maxi+3]

print("Puzzle 1: {}".format(puzzle1(adapters)))
print("Puzzle 2: {}".format(puzzle2(adapters)))
