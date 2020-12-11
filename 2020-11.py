#!/usr/bin/env python3

import numpy as np
from scipy.signal import convolve2d

from aoc import read_input

def apply_rules(occupied, seats):
    mask = np.array([[1,1,1],
                     [1,0,1],
                     [1,1,1]])
    
    neighbors = convolve2d(occupied, mask, mode='same')
    staying = occupied * (neighbors<4)
    sitting = (occupied==0) * (neighbors==0)
    
    return (staying + sitting) * seats

def puzzle1(seats):
    occupied = np.zeros(seats.shape)
    new_occupied = apply_rules(occupied, seats)
    while (occupied != new_occupied).any():
        occupied = new_occupied
        new_occupied = apply_rules(occupied, seats)
    
    return np.sum(occupied)

def puzzle2(seats):
    pass

raw = read_input(2020, 11).translate({76:'1', 46:'0'}).split()
seats = np.array([list(map(int, row)) for row in map(list, raw)])

print("Puzzle 1: {}".format(puzzle1(seats)))
print("Puzzle 2: {}".format(puzzle2(seats)))