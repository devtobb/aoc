#!/usr/bin/env python3
from math import sin, cos, pi, radians, atan2

from aoc import read_input


def execute(instr, x, y, d):
    direction, magnitude = instr

    if direction == 'N':
        y += magnitude
    elif direction == 'S':
        y -= magnitude
    elif direction == 'E':
        x += magnitude
    elif direction == 'W':
        x -= magnitude
    elif direction == 'L':
        d += magnitude
    elif direction == 'R':
        d -= magnitude
    elif direction == 'F':
        x += round(cos(radians(d)) * magnitude)
        y += round(sin(radians(d)) * magnitude)

    return x, y, d

def execute_relative(instr, x, y, wx, wy):
    direction, magnitude = instr

    if direction == 'N':
        wy += magnitude
    elif direction == 'S':
        wy -= magnitude
    elif direction == 'E':
        wx += magnitude
    elif direction == 'W':
        wx -= magnitude
    elif direction == 'L':
        angle = atan2(wy, wx)
        dist = (wx**2 + wy**2) ** 0.5
        wx = round(cos(radians(magnitude) + angle) * dist)
        wy = round(sin(radians(magnitude) + angle) * dist)
    elif direction == 'R':
        angle = atan2(wy, wx)
        dist = (wx**2 + wy**2) ** 0.5
        wx = round(cos(-radians(magnitude) + angle) * dist)
        wy = round(sin(-radians(magnitude) + angle) * dist)
    elif direction == 'F':
        x += wx * magnitude
        y += wy * magnitude

    return x, y, wx, wy

def puzzle1(instructions):
    x = y = d = 0
    for instr in instructions:
        x, y, d = execute(instr, x, y, d)
    
    return abs(x) + abs(y)

def puzzle2(instructions):
    x = y =  0
    wx = 10
    wy = 1
    for instr in instructions:
        x, y, wx, wy = execute_relative(instr, x, y, wx, wy)
        # print("Instr: {} Ship : ({}, {}) Waypoint: ({}, {})".format(instr, x, y, wx, wy))
    
    return abs(x) + abs(y)

raw = read_input(2020, 12)
instructions = [(row[0], int(row[1:])) for row in raw.split()]

print("Puzzle 1: {}".format(puzzle1(instructions)))
print("Puzzle 2: {}".format(puzzle2(instructions)))