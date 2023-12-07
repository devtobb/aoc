#!/usr/bin/env python3

from collections import Counter

from tools import read_input

ORDER = {False :  "23456789TJQKA", True :  "J23456789TQKA"}

class Hand(object):
    def __init__(self, line):
        self.cards, bid = line.split()
        self.bid = int(bid)

    def order(self, joker=False):
        cards = self.cards.replace('J', '') if joker else self.cards
        counter = Counter(cards)
        frequencies = sorted(counter.values(), reverse=True)
        most_frequent, second_most_frequent, *_ = frequencies + [0, 0]
        most_frequent += joker * self.cards.count('J')
        order = (most_frequent << 1) + second_most_frequent
        for card in self.cards:
            order = (order << 4) + ORDER[joker].index(card)
        return order
        
def score(hands, joker):
    hands = sorted(hands, key=lambda h: h.order(joker))
    return sum(n*hand.bid for n, hand in enumerate(hands, 1))

raw = read_input(2023, 7, 'bb').splitlines()
hands = tuple(map(Hand, raw))

print(f"\033[97m★\033[00m {score(hands, False)}")
print(f"\033[93m★\033[00m {score(hands, True)}")