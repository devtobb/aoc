#!/usr/bin/env python3

from collections import Counter

from tools import read_input

FIRST_SECOND = ((1,1),(2,1),(2,2),(3,1),(3,2),(4,1),(5,0))
LOOKUP = {t:n for n, t in enumerate(FIRST_SECOND)}
ORDER = {False :  "23456789TJQKA", True :  "J23456789TQKA"}

class Hand(object):
    def __init__(self, line):
        self.cards, bid = line.split()
        self.bid = int(bid)

    def _type(self, joker):
        cards = self.cards.replace('J', '') if joker else self.cards
        counter = Counter(cards)
        freq = sorted(counter.values(), reverse=True)
        first, second, *_ = freq + [0, 0]
        first += joker * self.cards.count('J')
        return LOOKUP[(first, second)]

    def order(self, joker=False):
        o = self._type(joker)
        for card in self.cards:
            o = (o << 4) + ORDER[joker].index(card)
        return o
        
def score(hands, joker):
    hands = sorted(hands, key=lambda h: h.order(joker))
    return sum(n*hand.bid for n, hand in enumerate(hands, 1))

raw = read_input(2023, 7, 'bb').splitlines()
hands = tuple(map(Hand, raw))

print(f"\033[97m★\033[00m {score(hands, False)}")
print(f"\033[93m★\033[00m {score(hands, True)}")