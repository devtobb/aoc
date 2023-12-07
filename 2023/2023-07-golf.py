from collections import Counter
from functools import reduce
from tools import read_input

def order(c, mask):
    c = c.translate(str.maketrans('TJQKA', mask))
    f, s, *_ = sorted(Counter(c.replace('0', '') if mask==':0<=>' else c).values(), reverse=True)+[0,0]
    return reduce(lambda o, ch: (o<<4) + ord(ch), c, ((f+(mask==':0<=>')*c.count('0'))<<1)+s)
        
raw = read_input(2023, 7, 'bb').split()
hands = [(cards, int(bid)) for cards, bid in zip(raw[::2], raw[1::2])]
for mask, color in ((':;<=>', 97), (':0<=>', 93)):
    print(f"\033[{color}m★\033[00m {sum(n*h[1] for n, h in enumerate(sorted(hands, key=lambda h: order(h[0], mask)), 1))}")
