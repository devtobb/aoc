#!/usr/bin/env python3

from itertools import cycle


from tools import *

class OneBasedCounter(object):
    def __init__(self, length, start=1):
        self._position = start - 1
        self.length = length

    def __add__(self, other):
        self._position = (self._position + other) % self.length
        return self.value

    @property
    def value(self):
        return self._position + 1

    @value.setter
    def value(self, v):
        self._position = (v - 1) % self.length

def puzzle1():
    pass

def puzzle2():
    pass

raw = read_input(2021, 21).splitlines()
(_, p1), (_, p2) = [ints(l) for l in raw] 

players = [OneBasedCounter(10, start=p1), OneBasedCounter(10, start=p2)]
score = [0, 0]
current = 0 
dice = OneBasedCounter(100, start=0)

n = 0
while all(s<1000 for s in score):
    rolls = dice+1,  dice + 1, dice + 1
    n += 3
    players[current] + sum(rolls)
    score[current] += players[current].value
    print(f"Player {current+1} rolls {'+'.join(map(str, rolls))} and moves to space {players[current].value} for a totel score of {score[current]}.")
    current = (current + 1) % 2

print(n, score[current], n*score[current])

print(f"\033[97m★\033[00m {puzzle1()}")
print(f"\033[93m★\033[00m {puzzle2()}")