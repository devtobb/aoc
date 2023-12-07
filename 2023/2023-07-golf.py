from collections import Counter
from functools import reduce
from tools import read_input

ORD = {False :  "23456789TJQKA", True :  "J23456789TQKA"}

def order(h, joker=False):
    f, s, *_ = sorted(Counter(h.replace('J', '') if joker else h).values(), reverse=True)+[0,0]
    f += joker * h.count('J')
    return reduce(lambda o, ch: (o<<4) + ORD[joker].index(ch), h, (f<<1)+s)
        
def score(hands, joker):
    return sum(n*h[1] for n, h in enumerate(sorted(hands, key=lambda h: order(h[0], joker)), 1))

raw = read_input(2023, 7, 'bb').split()
hands = [(cards, int(bid)) for cards, bid in zip(raw[::2], raw[1::2])]

print(f"\033[97m★\033[00m {score(hands, False)}")
print(f"\033[93m★\033[00m {score(hands, True)}")