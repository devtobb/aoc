#!/usr/bin/env python3

import re

from aoc import read_input

def contains(rules, bag, wanted):
    return (wanted in rules[bag] or 
            any(contains(rules, sub_bag, wanted) for sub_bag in rules[bag]))

def n_contains(rules, bag):
    if not rules[bag]:
        return 1

    return sum(rules[bag][sub_bag] * n_contains(rules, sub_bag) 
                for sub_bag in rules[bag]) + 1

def puzzle1(rules):
    return sum(contains(rules, bag, "shiny gold") for bag in rules)

def puzzle2(rules):
    return n_contains(rules, "shiny gold") - 1

raw = read_input(2020, 7).split('\n')[:-1]

r1 = r'(\w+ \w+) bags contain (.*)'
r2 = r'(\d+) (\w+ \w+)'

rules = dict(
            (k, dict((bag, int(count)) 
                for (count, bag) in re.findall(r2, v))
            )
                for k, v in map(lambda r: re.search(r1, r).groups(), raw)
        )

print("Puzzle 1: {}".format(puzzle1(rules)))
print("Puzzle 2: {}".format(puzzle2(rules)))