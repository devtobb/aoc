#!/usr/bin/env python3

import re

from aoc import read_input


lines = read_input(2023, 3).splitlines()
h = len(lines)
w = len(lines[0])

lines = ['.'+line+'.' for line in lines]
lines = ['.'*(w+2)] + lines +['.'*(w+2)]

h+=2
w+=2

def is_any_sym(t):
    return any((c not in '.1234567890' for c in t))

s1 = 0
for y in range(len(lines)):
    for m in re.finditer('\d+', lines[y]):
        start, end = m.span()
        if (
            is_any_sym(lines[y-1][start-1:end+1]) or
            is_any_sym(lines[y+1][start-1:end+1]) or
            is_any_sym(lines[y][start-1]) or
            is_any_sym(lines[y][end]) 
        ):
            s1 += int(m.group())


gears = [[[] for _ in range(w)] for _ in range(h)]

for y in range(h):
    for m in re.finditer(r'\d+', lines[y]):
        start, end = m.span()
        num = int(m.group())
        for dy in [-1, 0, 1]:
            for mg in re.finditer(r'\*', lines[y+dy][start-1:end+1]):
                g, _ = mg.span()
                gears[y+dy][start-1+g].append(num)

s2 = 0
for line in gears:
    for gear in line:
        if len(gear) == 2:
            s2 += gear[0]*gear[1]

print(f"\033[97m★\033[00m {s1}")
print(f"\033[93m★\033[00m {s2}")