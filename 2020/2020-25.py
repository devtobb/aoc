#!/usr/bin/env python3

from tools import read_input

def bf_loop_size(subject, pub):
    t = 1
    n = 0
    while t != pub:
        t = (t*subject) % 20201227
        n += 1

    return n

def enc_key(subject, n):
    t = 1
    for _ in range(n):
        t = (t*subject) % 20201227
    
    return t

def puzzle1(door, card):
    loop_size = bf_loop_size(7, door)
    return enc_key(card, loop_size)

def puzzle2():
    pass

raw = read_input(2020, 25)
door, card = list(map(int, raw.split()))

print(f"Puzzle 1: {puzzle1(door, card)}")
print(f"Puzzle 2: {puzzle2()}")