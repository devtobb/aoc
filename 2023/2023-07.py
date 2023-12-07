#!/usr/bin/env python3

from collections import Counter, namedtuple

from tools import read_input

ORDER = {False :  "23456789TJQKA", True :  "J23456789TQKA"}
Hand = namedtuple('Hand', ['cards', 'bid'])

def order(hand, joker=False):
    cards = hand.cards.replace('J', '') if joker else hand.cards
    counter = Counter(cards)
    frequencies = sorted(counter.values(), reverse=True)
    most_frequent, second_most_frequent, *_ = frequencies + [0, 0]
    most_frequent += joker * hand.cards.count('J')
    order = (most_frequent << 1) + second_most_frequent
    for card in hand.cards:
        order = (order << 4) + ORDER[joker].index(card)
    return order
        
def score(hands, joker):
    hands = sorted(hands, key=lambda hand: order(hand, joker))
    return sum(n*hand.bid for n, hand in enumerate(hands, 1))

raw = read_input(2023, 7, 'bb').split()
hands = [Hand(cards, int(bid)) for cards, bid in zip(raw[::2], raw[1::2])]

print(f"\033[97m★\033[00m {score(hands, False)}")
print(f"\033[93m★\033[00m {score(hands, True)}")