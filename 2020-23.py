#!/usr/bin/env python3

from aoc import read_input

def move(cups, current):
    idx_cur = cups.index(current)
    idx_pu_start = (idx_cur + 1) % len(cups)
    
    if len(cups) - idx_pu_start < 3:
        idx_pu_end = (idx_pu_start + 3) % len(cups)
        pu = cups[idx_pu_start:] + cups[:idx_pu_end]
        rest = cups[idx_pu_end:idx_pu_start]
    else:
        idx_pu_end = idx_pu_start + 3
        pu = cups[idx_pu_start:idx_pu_end]
        rest = cups[:idx_pu_start] + cups[idx_pu_end:]

    
    dest = current - 1
    while not dest in rest:
        dest -= 1
        if dest < min(rest):
            dest = max(rest)

    idx_dest = rest.index(dest)
    idx_dest = (idx_dest + 1) % len(cups)
    cups = rest[:idx_dest] + pu + rest[idx_dest:]
    idx_cur_new = cups.index(current)
    cur_new = cups[(idx_cur_new + 1)%len(cups)]
    
    return cups, cur_new

def puzzle1(cups):
    current, *_ = cups
    for _ in range(100):
        cups, current = move(cups, current)

    idx_one = cups.index(1)
    
    return "".join(map(str, cups[idx_one+1:] + cups[:idx_one]))

def puzzle2():
    pass

raw = read_input(2020, 23)
# raw = '389125467\n'
cups = list(map(int, list(raw[:-1])))


print(f"Puzzle 1: {puzzle1(cups)}")
print(f"Puzzle 2: {puzzle2()}")