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
        self.absolute = False
        self.position = np.array([0, 0, 0])

    def get_transform(self, other):
        if id(self) == id(other):
            print("trivial")
            return np.eye(3), np.array([0, 0, 0])

        for n, T in enumerate(transforms):
            coords_t = np.matmul(other.coords, T)
            deltas = dict()
            for point_self in self.coords:
                for point_other in coords_t:
                    dx, dy, dz = (point_self - point_other)
                    delta = (dx, dy, dz)
                    deltas[delta] = deltas.get(delta, 0) + 1

            for delta, count in deltas.items():
                if count >= 12:
                    print(f"Match for {self.title} and {other.title}: transform={n} delta={delta}")
                    return T, delta

        return None

    def apply_transform(self, T, delta):
        self.coords = np.matmul(self.coords, T) + delta
        self.position += delta
        self.absolute = True

    def distance(self, other):
        return sum(np.abs(self.position - other.position))

    def __str__(self):
        return str(self.coords)

    def __repr__(self):
        return f"<Scanner: {str(self)}>"

def puzzle1(scanners):
    return len(beacons)

def puzzle2():
    return max( f.distance(s) for f, s in product(scanners, scanners))

raw = read_input(2021, 19)
blocks = raw.split("\n\n")
scanners = tuple(map(Scanner, blocks))    

scanners[0].absolute = True
queue = [scanners[0]]
while len(queue) > 0:
    first = queue.pop()
    for second in scanners:
        if not second.absolute:
            transform = first.get_transform(second)
            if transform is not None:
                T, delta = transform
                second.apply_transform(T, delta)
                queue.append(second)

beacons = { (x, y, z) for scanner in scanners for x,y,z in scanner.coords}


print(f"\033[97m★\033[00m {puzzle1(scanners)}")
print(f"\033[93m★\033[00m {puzzle2()}")