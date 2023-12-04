#!/usr/bin/env python3

from functools import cached_property
import re

from aoc import read_input

class Card:
    def __init__(self, line):
        _, numbers = line.split(':')
        win, have = numbers.split('|')
        
        self.win = tuple(map(int, win.split()))
        self.have = tuple(map(int, have.split()))
        self.count = 1
    
    @cached_property
    def n_matching(self):
        return sum(n in self.win for n in self.have)

    @property
    def points(self):
        return 2**(self.n_matching - 1) if self.n_matching > 0 else 0

def puzzle1(cards):
    return sum(card.points for card in cards)
        
def puzzle2(cards):
    for n, card in enumerate(cards, 1):
        for dupe in cards[n:n+card.n_matching]:
            dupe.count += card.count

    return sum(card.count for card in cards)

lines = read_input(2023, 4).splitlines()
cards = list(map(Card, lines))

print(f"\033[97m★\033[00m {puzzle1(cards)}")
print(f"\033[93m★\033[00m {puzzle2(cards)}")