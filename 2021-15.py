#!/usr/bin/env python3

from queue import PriorityQueue

import numpy as np

from aoc import read_input

def neighbors(p, shape):
    wy, wx = shape
    py, px = p
    for ny, nx in (-1, 0), (1, 0), (0, -1), (0, 1):
        y, x = py + ny, px + nx
        if x >= 0 and x<wx and y>=0 and y<wy:
            yield (y, x)

def spread(m):
    col = m
    for n in range(1, 5):
        col = np.concatenate((col, ((m-1+n)%9)+1))

    ret = col
    for n in range(1, 5):
        ret = np.concatenate((ret, ((col-1+n)%9)+1), axis=1)

    return ret

def min_dist(p1, p2):
    p1y, p1x = p1
    p2y, p2x = p2
    return abs(p1y - p2y) + abs(p1x - p2x)


def a_star(cave):
    wy, wx = cave.shape
    current = (0, 0)
    destination = (wy-1, wx-1)

    distance = np.zeros(cave.shape) + float('inf')
    distance[current] = 0
    visited = np.zeros(cave.shape)

    to_visit = PriorityQueue()
    to_visit.put((min_dist(current, destination), current))
    to_visit_set = set([current])

    while current != destination:
        for neigh in neighbors(current, cave.shape):
            if not visited[neigh]:
                dist = distance[current] + cave[neigh]
                distance[neigh] = min(distance[neigh], dist)
                if neigh not in to_visit_set:
                    to_visit.put((distance[neigh] + min_dist(neigh, destination), neigh))
                    to_visit_set.add(neigh)
        visited[current] = True
        to_visit_set.discard(current)
        _, current = to_visit.get()

    return int(distance[-1, -1])


def puzzle1(cave):
    return a_star(cave)

def puzzle2(cave):
    cave = spread(cave)
    return a_star(cave)

raw = read_input(2021, 15)
cave = np.array(list(map(list, raw.split())), dtype=int)

print(f"\033[97m★\033[00m {puzzle1(cave)}")
print(f"\033[93m★\033[00m {puzzle2(cave)}")