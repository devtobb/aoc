#!/usr/bin/env python3

from itertools import chain
import re

from tools import *

def sum_invalid_ids(ranges, regex):
    ids = chain.from_iterable([range(l, h+1) for l, h in ranges])
    return sum(filter(lambda i:regex.match(str(i)), ids))

def puzzle1(ranges):
    return sum_invalid_ids(ranges, re.compile(r"^(\d+)\1$"))

def puzzle2(ranges):
    return sum_invalid_ids(ranges, re.compile(r"^(\d+)\1{1,}$"))

raw = read_input(2025, 2)
ranges = [tuple(map(int, rng.split("-"))) for rng in raw.split(",")]

print(f"\033[97m★\033[00m {puzzle1(ranges)}")
print(f"\033[93m★\033[00m {puzzle2(ranges)}")