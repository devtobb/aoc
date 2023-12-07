#!/usr/bin/env python3

from collections import Counter
from functools import cached_property

from tools import read_input

lookup = {t:n for n, t in enumerate(((1,1),(2,1),(2,2),(3,1),(3,2),(4,1),(5,0)))}

class Hand(object):
    CARDS = "23456789TJQKA"

    def __init__(self, line):
        self.cards, bid = line.split()
        self.bid = int(bid)

    def _type(self):
        *_, second, first = [0] + sorted(Counter(self.cards).values())
        return lookup[(first, second)]

    @cached_property
    def order(self):
        o = self._type()
        for card in self.cards:
            o = (o << 4) + self.CARDS.index(card)
        return o

class HandJoker(Hand):
    CARDS = "J23456789TQKA"

    def _type(self):
        frequencies = sorted(Counter(self.cards.replace('J', '')).values(), reverse=True)
        first, second, *_  =  frequencies + [0, 0]
        first += self.cards.count('J')
        return lookup[(first, second)]
    
def score(hands):
    return sum(n*hand.bid for n, hand in enumerate(sorted(hands, key=lambda h: h.order), 1))

raw = read_input(2023, 7, 'bb').splitlines()
hands = tuple(map(Hand, raw))
hands_joker = tuple(map(HandJoker, raw))

print(f"\033[97m★\033[00m {score(hands)}")
print(f"\033[93m★\033[00m {score(hands_joker)}")