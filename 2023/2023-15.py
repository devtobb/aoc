#!/usr/bin/env python3

from functools import reduce

from tools import *

def hsh(chars):
    return reduce(lambda h, c: ((h+c)*17)%256, map(ord, chars), 0)

def puzzle1(seqs):
    return sum(map(hsh, seqs))

def puzzle2(seqs):
    boxes = [{} for _ in range(256)]

    for seq in seqs:
        if '-' in seq:
            label = seq[:-1]
            boxes[hsh(label)].pop(label, None)
        else:
            label = seq[:-2]
            f = int(seq[-1])
            boxes[hsh(label)][label] = f

    fp = 0
    for n, box in enumerate(boxes, 1):
        for m, lens in enumerate(box, 1):
            fp += n * m * box[lens]
    
    return fp

raw = read_input(2023, 15, '').replace('\n', '')
seqs = raw.split(',')

print(f"\033[97m★\033[00m {puzzle1(seqs)}")
print(f"\033[93m★\033[00m {puzzle2(seqs)}")