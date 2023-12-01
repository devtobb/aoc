#!/usr/bin/env python3

from aoc import read_input

def evaluate_p1(expr):
    n = sum(expr.count(c) for c in "+*")
    return eval('('*(n+2) + expr.translate({40:'('*n,41:')'*n,42:'))*(',43:'))+('})+'))')

def evaluate_p2(expr):
    return eval('((' + expr.translate({40:'(((',41:')))',42:'))*((',43:')+('})+'))')

def puzzle1(expressions):
    return sum(evaluate_p1(expr) for expr in expressions)

def puzzle2(expressions):
    return sum(evaluate_p2(expr) for expr in expressions)

expressions = read_input(2020, 18).split('\n')[:-1]

print(f"Puzzle 1: {puzzle1(expressions)}")
print(f"Puzzle 2: {puzzle2(expressions)}")