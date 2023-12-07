#!/usr/bin/env python3

from itertools import product
from functools import reduce

import numpy as np

from tools import read_input

Rx = np.array([[1,0,0],[0,0,-1],[0,1,0]])
Ry = np.array([[0,0,1],[0,1,0],[-1,0,0]])
Rz = np.array([[0,-1,0],[1,0,0],[0,0,1]])

transforms = [
    reduce(np.matmul, chain, np.eye(3, dtype=int))
    for Cz in [
        [],
        [Rz],
        [Rz, Rz],
        [Rz, Rz, Rz]
    ]
    for chain in [
        [] + Cz,
        [Rx] + Cz,
        [Rx, Rx] + Cz,
        [Rx, Rx, Rx] + Cz,
        [Ry] + Cz,
        [Ry, Ry, Ry] + Cz,
    ] 
]

class Scanner(object):

    def __init__(self, block: str):
        self.title, *lines = block.splitlines()
        lines = [list(map(int, line.split(','))) for line in lines]
        self.coords = np.array(lines)

    def __eq__(self, other):
        if id(self) == id(other):
            print("trivial")
            return True
        # set_other = {str(b) for b in other.coords}
        for n, T in enumerate(transforms):
            coords_t = np.matmul(self.coords, T)
            # set_own = {str(b) for b in coords_t}
            deltas = dict()
            for point_self in coords_t:
                for point_other in other.coords:
                    delta = str(point_self - point_other)
                    deltas[delta] = deltas.get(delta, 0) + 1

            for count in deltas.values():
                if count >= 12:
                    print(f"Match for {self.title} and {other.title}: transform={n}")
                    return True

        return False

    def __str__(self):
        return str(self.coords)

    def __repr__(self):
        return f"<Scanner: {str(self)}>"

def puzzle1(scanners):
    for n, first in enumerate(scanners):
        for second in scanners[n+1:]:
            if first == second:
                pass

def puzzle2():
    pass

raw = read_input(2021, 19)
blocks = raw.split("\n\n")
scanners = tuple(map(Scanner, blocks))    

print(f"\033[97m★\033[00m {puzzle1(scanners)}")
print(f"\033[93m★\033[00m {puzzle2()}")