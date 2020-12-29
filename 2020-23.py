#!/usr/bin/env python3

from aoc import read_input

def neighbors(cups):
    neigh = dict(zip(cups[:-1], cups[1:]))
    neigh[cups[-1]] = cups[0]
    return neigh

def move(neigh, current, min_, max_):
    pickup = [neigh[current], neigh[neigh[current]], neigh[neigh[neigh[current]]]]
    pickup_first, _, pickup_last= pickup
    
    destination = current - 1
    if destination < min_:
        destination = max_
    while destination in pickup:
        destination -= 1
        if destination < min_:
            destination = max_

    neigh[destination], neigh[pickup_last], neigh[current] = (
        pickup_first, neigh[destination], neigh[pickup_last])

    return neigh, neigh[current]

def run(cups, n_rounds):
    neigh = neighbors(cups)
    current, *_ = cups
    min_, max_ = min(cups), max(cups)
    for _ in range(n_rounds):
        neigh, current = move(neigh, current, min_, max_)

    return neigh

def puzzle1(cups):
    neigh = run(cups, 100)
    current, ret = 1, ''
    for _ in range(8):
        ret += str(current:=neigh[current])

    return ret

def puzzle2(cups):
    cups = cups + list(range(10, 1_000_001))
    neigh = run(cups, 10_000_000)
    
    return neigh[1] * neigh[neigh[1]]

raw = read_input(2020, 23)
cups = list(map(int, list(raw[:-1])))

print(f"Puzzle 1: {puzzle1(cups)}")
print(f"Puzzle 2: {puzzle2(cups)}")