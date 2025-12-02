#!/usr/bin/env python3

from math import floor, log10

from tools import *

def range_stats(ranges):
    invalid = []
    for l, h in ranges:
        l_dec = floor(log10(l)) + 1
        h_dec = floor(log10(h)) + 1
        v_dec = [n for n in range(l_dec, h_dec + 1) if n%2==0]
        
        slower = 10**(l_dec-1) if l_dec%2==0 else 10**l_dec
        slower = max(slower, l)

        supper = 10**(h_dec - 1) - 1 if h_dec%2!=0 else h

        start = int(slower//(10**((floor(log10(slower))+1)/2)))
        end = int(supper//(10**((floor(log10(supper))+1)/2)))

        print(f"{l} - {h} [{h-l}] -- {l_dec}-{h_dec} ({v_dec}) #{slower}-{supper} --- {start} -> {end}")

        for n in range(start, end+1):
            p = n*10**(floor(log10(n))+1)+n
            if p>=l and p<=h:
                print(f"\t{p}")
                invalid.append(p)

    return invalid

def puzzle1(ranges):
    invalid = range_stats(ranges)
    return sum(invalid)

def puzzle2(ranges):
    invalid = []
    regex = re.compile(r"^(\d+)\1{1,}$")
    for l, h in ranges:
        print(f"{l} - {h} ({h-l})")
        for n in range(l, h+1):
            if regex.match(str(n)):
                invalid.append(n)
    return(sum(invalid))


raw = read_input(2025, 2)
ranges = [tuple(map(int, rng.split("-"))) for rng in raw.split(",")]

print(f"\033[97m★\033[00m {puzzle1(ranges)}")
print(f"\033[93m★\033[00m {puzzle2(ranges)}")