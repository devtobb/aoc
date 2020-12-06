#!/usr/bin/env python3

import re

from aoc import read_input

def puzzle1(passports, valid):
    return sum(all(key in passport for key in valid) for passport in passports)

def puzzle2(passports, valid):
    return sum(all(re.match(valid[key], passport[key]) 
                        if key in passport else None 
                    for key in valid) 
                for passport in passports
    )

raw = read_input(2020, 4).split('\n\n')
passports = [dict(re.findall(r"(\S{3})\:(\S+)", p)) for p in raw]

valid = dict(
    byr = r'^19[2-9]\d|200[0-2]$',
    iyr = r'^20(1\d|20)$',
    eyr = r'^20(2\d|30$)',
    hgt = r'^(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)$',
    hcl = r'^#[0-9a-f]{6}$',
    ecl = r'^amb|blu|brn|gry|grn|hzl|oth$',
    pid = r'^\d{9}$'
)

print("Puzzle 1: {}".format(puzzle1(passports, valid)))
print("Puzzle 2: {}".format(puzzle2(passports, valid)))