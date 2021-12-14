#!/usr/bin/env python3

from collections import defaultdict
from math import ceil
import re

from gmpy2 import mpz
import numpy as np


from aoc import read_input

def fast_exp(m, p):
    if p==1:
        return m
    else:
        ret = fast_exp(m, p//2)
        ret = ret @ ret
        if p%2 > 0:
            ret = ret @ fast_exp(m, p%2)
        return ret

def synthesize(start, subs, elements, rounds):
    pairs = [a+b for a in elements for b in elements]
    n_elements = len(elements)

    m = np.zeros((n_elements**2,)*2, dtype=mpz)

    for (e1, e2), e3 in subs.items():
        m[pairs.index(e1+e2)][pairs.index(e1+e3)] += 1
        m[pairs.index(e1+e2)][pairs.index(e3+e2)] += 1

    v = np.zeros(n_elements**2, dtype=mpz)
    for e1, e2 in zip(start, start[1:]):
        v[pairs.index(e1+e2)] += 1

    result = v @ fast_exp(m, rounds)

    count = defaultdict(mpz)
    for e1, e2 in pairs:
        count[e1] += result[pairs.index(e1+e2)]
        count[e2] += result[pairs.index(e1+e2)]

    least, *_, most = sorted(map(lambda c: ceil(c/2), count.values()))

    return int(most - least)

raw = read_input(2021, 14)
start, subs = raw.split('\n\n')
subs = dict(re.findall("(\w+) -> (\w)+", subs))
elements = list(set(re.findall("\w", raw)))

print(f"\033[97m★\033[00m {synthesize(start, subs, elements, 10)}")
print(f"\033[93m★\033[00m {synthesize(start, subs, elements, 40)}")