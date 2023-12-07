#!/usr/bin/env python3

from itertools import product

from tools import read_input

def run_code(code, in1, in2):
    code = code.copy()
    code[1] = in1
    code[2] = in2
    pos = 0
    while code[pos] != 99:
        if code[pos] == 1:
            op = lambda a, b: a + b
        elif code[pos] == 2:
            op = lambda a, b,: a * b
        else:
            raise RuntimeError('Wrong op code at {}\nCode:\n{}'.format(pos, code))
        code[code[pos+3]] = op(code[code[pos+1]], code[code[pos+2]])
        pos+=4

    return code[0]

def puzzle1(code):
    return run_code(code, 12, 2)
    

def puzzle2(code):
    for a, b in product(range(100), range(100)):
        result = run_code(code, a, b)
        if result == 19690720:
            return a*100 + b

code = list(map(int, read_input(2019, 2).split(',')))

print("Puzzle 1: {}".format(puzzle1(code)))
print("Puzzle 2: {}".format(puzzle2(code)))