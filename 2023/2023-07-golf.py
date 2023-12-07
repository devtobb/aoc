from collections import Counter
from functools import reduce
from tools import read_input

def order(c, m):
    c = c.translate(str.maketrans('TJQKA', m))
    f = [0,0]+sorted(Counter(c.replace('0','') if m==':0<=>' else c).values())
    return (((f[-1]+(mask==':0<=>')*c.count('0'))<<1)+f[-2]), c
        
raw, e, s = read_input(2023, 7, 'bb').split(), enumerate, sorted
hd = [(cards, int(bid)) for cards, bid in zip(raw[::2], raw[1::2])]
for mask in ':;<=>', ':0<=>':
    print(sum(n*h[1] for n, h in e(s(hd, key=lambda h: order(h[0], mask)), 1)))
