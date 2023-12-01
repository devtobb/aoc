#!/usr/bin/env python3

import re

from aoc import read_input

words = 'one|two|three|four|five|six|seven|eight|nine'
lookup = dict(zip(words.split('|'), '123456789'))


def value_sum(regex, lines):

    def value(line):
        token = re.findall(regex, line)
        first, *_ = token
        *_, last = token
        return int(lookup.get(first, first) + lookup.get(last, last))

    return sum(map(value, lines))

def puzzle1(lines):
    return value_sum(r'\d', lines)

def puzzle2(lines):
    return value_sum(f'(?=({words}|\d))', lines)

raw = read_input(2023, 1)
lines = raw.split()

print(f"\033[97m★\033[00m {puzzle1(lines)}")
print(f"\033[93m★\033[00m {puzzle2(lines)}")