#!/usr/bin/env python3

from collections import defaultdict, Counter
from math import ceil
import re

from gmpy2 import mpz
import numpy as np


from aoc import read_input

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

    result = v @ np.linalg.matrix_power(m, rounds)

    count = defaultdict(mpz)
    for e1, e2 in pairs:
        count[e1] += result[pairs.index(e1+e2)]
        count[e2] += result[pairs.index(e1+e2)]

    least, *_, most = sorted(map(lambda c: ceil(c/2), count.values()))

    return most - least

raw = read_input(2021, 14)
start, subs = raw.split('\n\n')
subs = dict(re.findall("(\w+) -> (\w)+", subs))
elements = list(set(re.findall("\w", raw)))

print(f"\033[97m★\033[00m {synthesize(start, subs, elements, 65_536)}")
# print(f"\033[93m★\033[00m {synthesize(start, subs, elements, 40)}")