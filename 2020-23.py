#!/usr/bin/env python3

from aoc import read_input

class blist(list):
    def __rshift__(self, f):
        if type(f)==tuple: f, *args = f
        else: args = ()
        return blist(f(x, *args) for x in self)

def move(cups, current):
    idx_cur, *_ = [n for n, cup in enumerate(cups) if cup==current]
    idx_pu_start = (idx_cur + 1) % len(cups)
    if len(cups) - idx_pu_start < 3:
        idx_pu_end = (idx_pu_start + 3) % len(cups)
    else:
        idx_pu_end = idx_pu_start + 3

    if idx_pu_start < idx_pu_end:
        pu = cups[idx_pu_start:idx_pu_end]
        rest = cups[:idx_pu_start] + cups[idx_pu_end:]
    else:
        pu = cups[idx_pu_start:] + cups[:idx_pu_end]
        rest = cups[idx_pu_end:idx_pu_start]
    
    dest = current - 1
    while not dest in rest:
        dest -= 1
        if dest < min(rest):
            dest = max(rest)

    idx_dest, *_ = [n for n, cup in enumerate(rest) if cup==dest]

    idx_dest = (idx_dest + 1) % len(cups)

    # print(f"cups: {cups} current: {current}")
    # print(f"pu: {pu} [{idx_pu_start}, {idx_pu_end}]")
    # print(f"dest: {dest} ({idx_dest})")

    ret = rest[:idx_dest] + pu + rest[idx_dest:]
    # print(f"ret: {ret}")
    # print()
    idx_cur_new, *_ = [n for n, cup in enumerate(ret) if cup==current]
    cur_new = ret[(idx_cur_new + 1)%len(cups)]
    
    return ret, cur_new

def puzzle1(cups):
    current, *_ = cups
    for _ in range(100):
        cups, current = move(cups, current)

    idx_one, *_ = [n for n, cup in enumerate(cups) if cup==1]
    
    return "".join(blist((cups[idx_one+1:] + cups[:idx_one])) >> str)

def puzzle2():
    pass

raw = read_input(2020, 23)
# raw = '389125467\n'
cups = blist(raw[:-1]) >> int


print(f"Puzzle 1: {puzzle1(cups)}")
print(f"Puzzle 2: {puzzle2()}")