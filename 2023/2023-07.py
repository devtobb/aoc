#!/usr/bin/env python3

from collections import Counter
from functools import total_ordering, cache
from itertools import combinations_with_replacement

hand_type = ['HIGH_CARD', 'ONE_PAIR', 'TWO_PAIR', 'THREE', 'FULL_HOUSE', 'FOUR', 'FIVE']
lookup_type = {t:n for n, t in enumerate(((1,1),(2,1),(2,2),(3,1),(3,2),(4,1),(5,0)))}

from tools import read_input

@total_ordering
class Hand(object):
    
    CARDS = "23456789TJQKA"

    def __init__(self, line):
        self.cards, bid = line.split()
        self.bid = int(bid)

    @property
    def typ(self):
        return self.calculate_typ(self.cards)

    @staticmethod
    @cache
    def calculate_typ(cards):
        *_, second, first = [0] + sorted(Counter(cards).values())
        return lookup_type[(first, second)]

    def __eq__(self, other):
        return self.cards == other.cards
    
    def __lt__(self, other):
        if self.typ != other.typ:
            return self.typ < other.typ
        for card_self, card_other in zip(self.cards, other.cards):
            if card_self != card_other:
                return self.CARDS.index(card_self) < self.CARDS.index(card_other)
        return False
        
    def __str__(self):
        return f"{self.cards} ({self.bid}) [{str(hand_type[self.typ])}]"

    def __repr__(self):
        return f"<Hand: {str(self)}>"

class HandJoker(Hand):

    CARDS = "J23456789TQKA"

    @staticmethod
    @cache
    def calculate_typ(cards):
        *_, second, first = [0, 0] + sorted(Counter(cards.replace('J', '')).values())
        first += cards.count('J')
        return lookup_type[(first, second)]
    
def score(hands):
    return sum(n*hand.bid for n, hand in enumerate(sorted(hands), 1))

raw = read_input(2023, 7).splitlines()
hands = list(map(Hand, raw))
hands_joker = list(map(HandJoker, raw))

print(f"\033[97m★\033[00m {score(hands)}")
print(f"\033[93m★\033[00m {score(hands_joker)}")