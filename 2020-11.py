#!/usr/bin/env python3

from itertools import product

import numpy as np
from scipy.signal import convolve2d

from aoc import read_input

def coords(start, direction, shape):
    height, width = shape
    y, x = start
    dy, dx = direction
    while True:
        y += dy
        x += dx
        if not(0<=y< height and 0<=x<width):
            break
        yield y, x

def neighbors_puzzle2(occupied, seats):
    neighbors = np.zeros(occupied.shape)
    for y, x in product(*list(map(range ,occupied.shape))):
       for direction in ((1,0),(0,1),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)):
           for ty, tx in coords((y,x), direction, occupied.shape):
                if occupied[ty,tx]:
                    neighbors[y,x] += 1
                    break
                if seats[ty, tx]:
                    break
                
    
    return neighbors

def neighbors_puzzle1(occupied, seats):
    mask = np.array([[1,1,1],
                     [1,0,1],
                     [1,1,1]])
    
    return convolve2d(occupied, mask, mode='same')

def apply_rules(occupied, seats, max_neighbors, neighbor_func):
    
    neighbors = neighbor_func(occupied, seats)
    staying = occupied * (neighbors <= max_neighbors)
    sitting = (occupied == 0) * (neighbors == 0)
    return (staying + sitting) * seats

def equilibrium_sum(seats, max_neighbors, neighbor_func):
    occupied = np.zeros(seats.shape)
    while True:
        new_occupied = apply_rules(occupied, seats, max_neighbors, neighbor_func)
        if (occupied == new_occupied).all(): break
        occupied = new_occupied
    
    return np.sum(occupied)

def puzzle1(seats):
    return equilibrium_sum(seats, 3, neighbors_puzzle1)

def puzzle2(seats):
    return equilibrium_sum(seats, 4, neighbors_puzzle2)

raw = read_input(2020, 11).translate({76:'1', 46:'0'}).split()
seats = np.array([list(map(int, row)) for row in map(list, raw)])

print("Puzzle 1: {}".format(puzzle1(seats)))
print("Puzzle 2: {}".format(puzzle2(seats)))