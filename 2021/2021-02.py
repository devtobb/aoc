#!/usr/bin/env python3

from tools import read_input

def puzzle1(raw):
    fwd = filter(lambda s: s['d']=='forward', raw)
    updown = filter(lambda s: s['d']!='forward', raw)
    fwd_total =  sum((s['m'] for s in fwd))
    updown_total = sum((s['m'] if s['d']=='down' else -s['m'] for s in updown))
    return fwd_total * updown_total

def puzzle2(raw):
    hor = dep = aim = 0
    for s in raw:
        if s['d'] == 'down':
            aim += s['m']
        if s['d'] == 'up':
            aim -= s['m']
        if s['d'] == 'forward':
            hor += s['m']
            dep += aim * s['m']
    return dep * hor

raw = read_input(2021, 2).split('\n')[:-1]
raw = list(map(lambda s: dict(d=s.split()[0],m=int(s.split()[1])),  raw))

print(f"Puzzle 1: {puzzle1(raw)}")
print(f"Puzzle 2: {puzzle2(raw)}")