#!/usr/bin/env python3

from functools import cache

from tools import *

@cache
def arrangs(springs, counts):
    assert type(springs) == tuple
    assert type(counts) == tuple

    if len(counts) == 0:
        return int('#' not in springs)
    if len(springs) == 0:
        return 0
    if sum(counts) > len(springs):
        return 0

    first_char = springs[0]
    rest_chars = springs[1:]
    next_len, *_ = counts

    match first_char:
        case '.':
            return arrangs(rest_chars, counts)
        case '#':
            if len(springs) < next_len:
                return 0
            elif len(springs) == next_len and '.' not in springs:
                return len(counts) == 1
            if '.' not in springs[:next_len] and springs[next_len] != '#':
                return arrangs(springs[next_len+1:], counts[1:])
            else:
                return 0
        case '?':
            return arrangs(rest_chars, counts) + arrangs(('#',) + rest_chars, counts)
    
    assert False, "Can't end up here"

raw = read_input(2023, 12)
records = [line.split() for line in raw.splitlines()]
records = [(tuple(springs), tuple(ints(counts))) for springs, counts in records]

records_five = [ (  tuple('?'.join([''.join(springs)]*5)), counts*5) for springs, counts in records]

s1 = sum(arrangs(springs, counts) for springs, counts in records)
s2 = sum(arrangs(springs, counts) for springs, counts in records_five)

print(f"\033[97m★\033[00m {s1}")
print(f"\033[93m★\033[00m {s2}")