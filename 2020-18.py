#!/usr/bin/env python3

from operator import mul, add
import re

from aoc import read_input

def evaluate(expr):
    # print(f"Evaluating: {expr}")
    num_op_re = r'(.*) (\+|\*) (\d+)$'
    num_re = r'^(\d+)$'
    operators = {'*':mul, '+':add}

    num_op_match = re.match(num_op_re, expr)
    num_match = re.match(num_re, expr)
    if num_op_match:
        rest, operator, operand = num_op_match.groups()
        return operators[operator](int(operand), evaluate(rest))
    elif num_match:
        num, *_ = num_match.groups()
        return int(num)
    else:
        n=len(expr)-2
        closing = 1
        while closing:
            if expr[n]=='(': closing -= 1
            if expr[n]==')': closing += 1
            n -= 1
        return evaluate(expr[:n+1] + str(evaluate(expr[n+2:-1])))
        # return evaluate(str(evaluate(expr[1:n-1])) + expr[n:])


def repleval(expr, repls):
    for repl in repls:
        expr = expr.replace(repl, repls[repl])
    expr = "["*(expr.count('*')+expr.count('+')+1) + expr + ']'
    return expr.replace(']', ')').replace('[', '(')

def repleval2(expr, repls):
    for repl in repls:
        expr = expr.replace(repl, repls[repl])
    expr = "[[" + expr + ']]'
    return eval(expr.replace(']', ')').replace('[', '('))


def puzzle1(expressions):
    return sum(evaluate(expr) for expr in expressions)

def puzzle2(expressions):
    d = {
        " + ": "] + [", 
        " * ": "]] * [[",
        "(" : "[[[",
        ")" : "]]]"
    }
    return sum(repleval2(expr, d) for expr in expressions)

expressions = read_input(2020, 18).split('\n')[:-1]

print(f"Puzzle 1: {puzzle1(expressions)}")
print(f"Puzzle 2: {puzzle2(expressions)}")