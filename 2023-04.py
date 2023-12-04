#!/usr/bin/env python3

from functools import cached_property
import re

from aoc import read_input

class Card:
    def __init__(self, line):
        _, numbers = line.split(':')
        win, have = numbers.split('|')
        
        self.win = list(map(int, win.split()))
        self.have = list(map(int, have.split()))
        self.count = 1
    
    @cached_property
    def n_matching(self):
        return sum(1 for n in self.have if n in self.win)

    @property
    def points(self):
        return 2**(self.n_matching - 1) if self.n_matching > 0 else 0

def puzzle1(cards):
    return sum(card.points for card in cards)
        
def puzzle2(cards):
    for n, card in enumerate(cards):
        for dupe in cards[n+1:n+1+card.n_matching]:
            dupe.count += card.count

    return sum(card.count for card in cards)

lines = read_input(2023, 4).splitlines()
cards = list(map(Card, lines))

print(f"\033[97m★\033[00m {puzzle1(cards)}")
print(f"\033[93m★\033[00m {puzzle2(cards)}")