#!/usr/bin/env python3

import re

from tools import read_input

def is_any_sym(t):
    return any((c not in '.1234567890' for c in t))

def puzzle1(lines):
    _sum = 0
    for n, line in enumerate(lines):
        for m in re.finditer('\d+', line):
            start, end = m.span()
            if (
                is_any_sym(lines[n-1][start-1:end+1]) or
                is_any_sym(lines[n+1][start-1:end+1]) or
                is_any_sym(lines[n][start-1]) or
                is_any_sym(lines[n][end]) 
            ):
                _sum += int(m.group())
    return _sum

def puzzle2(lines):
    height = len(lines)
    width = len(lines[0])
    
    gears = [[[] for _ in range(width)] for _ in range(height)]

    for n, line in enumerate(lines):
        for m in re.finditer(r'\d+', line):
            start, end = m.span()
            num = int(m.group())
            for delta in [-1, 0, 1]:
                for mg in re.finditer(r'\*', lines[n+delta][start-1:end+1]):
                    g, _ = mg.span()
                    gears[n+delta][start-1+g].append(num)

    _sum = 0
    for line in gears:
        for gear in line:
            if len(gear) == 2:
                _sum += gear[0]*gear[1]
    
    return(_sum)


lines = read_input(2023, 3).splitlines()
width = len(lines[0])
lines = ['.'+line+'.' for line in lines]
lines = ['.'*(width+2)] + lines +['.'*(width+2)]

print(f"\033[97m★\033[00m {puzzle1(lines)}")
print(f"\033[93m★\033[00m {puzzle2(lines)}")