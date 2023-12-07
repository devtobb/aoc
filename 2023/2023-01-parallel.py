#!/usr/bin/env python3

import re
from multiprocessing import Pool

from tools import read_input

words = 'one|two|three|four|five|six|seven|eight|nine'
lookup = dict(zip(words.split('|'), '123456789'))

pattern1 = re.compile(r'\d')
pattern2 = re.compile(f'(?=({words}|\d))')

def value1(line):
    token = pattern1.findall(line)
    first, *_ = token
    *_, last = token
    return int(lookup.get(first, first) + lookup.get(last, last))

def value2(line):
    token = pattern2.findall(line)
    first, *_ = token
    *_, last = token
    return int(lookup.get(first, first) + lookup.get(last, last))

raw = read_input(2023, 1)
lines = raw.split()

with Pool(processes=4) as pool:
    sum1 = sum(pool.map(value1, lines))

with Pool(processes=4) as pool:
    sum2 = sum(pool.map(value2, lines))

print(f"\033[97m★\033[00m {sum1}")
print(f"\033[93m★\033[00m {sum2}")