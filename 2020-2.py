import re

from aoc import read_input

def valid_puzzle1(p):
    c = p['pass'].count(p['l'])
    return c >= int(p['a']) and c <= int(p['b'])

def valid_puzzle2(p):
    l1 = p['pass'][int(p['a']) - 1]
    l2 = p['pass'][int(p['b']) - 1]
    return (p['l'] == l1) != (p['l'] == l2)

def puzzle1(pass_list):
    return len(list(filter(valid_puzzle1, pass_list)))

def puzzle2(pass_list):
    return len(list(filter(valid_puzzle2, pass_list)))

r = r"(?P<a>\d+)-(?P<b>\d+)\s(?P<l>\w)\:\s(?P<pass>[^\n]+)"
pass_list = [m.groupdict() for m in re.finditer(r, read_input(__file__))]

print("Puzzle 1: {}".format(puzzle1(pass_list)))
print("Puzzle 2: {}".format(puzzle2(pass_list)))

