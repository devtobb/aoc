#!/usr/bin/env python3

from aoc import read_input

def count_trees(field, slope=(3, 1)):
    dx, dy = slope
    height = len(field)
    width = len(field[0])

    coords = ((y // dy * dx % width, y) for y in range(0, height, dy))

    return sum((1 if field[y][x] == "#" else 0 for (x, y) in coords))

def puzzle1(field):
    return count_trees(field)

def puzzle2(field):
    return (count_trees(field) *
            count_trees(field, slope=(1, 1)) *
            count_trees(field, slope=(5, 1)) *
            count_trees(field, slope=(7, 1)) *
            count_trees(field, slope=(1, 2))
    )

field = read_input(__file__).split()

print("Puzzle 1: {}".format(puzzle1(field)))
print("Puzzle 2: {}".format(puzzle2(field)))