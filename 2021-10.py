#!/usr/bin/env python3

from statistics import median

from aoc import read_input

opening = '([{<'
closing = ')]}>'
score_corrupt = {')':3, ']':57, '}':1197, '>':25137}
score_incomplete = {'(':1, '[':2, '{':3, '<':4}

def puzzles(lines):
    sum_corrupt = 0
    scores_incomplete = []
    for line in lines:
        stack = []
        corrupt = False
        for c in line:
            if c in opening:
                stack.append(c)
            else:
                if stack and closing.index(c) == opening.index(stack[-1]):
                    stack.pop()
                else:
                    sum_corrupt += score_corrupt[c]
                    corrupt = True
                    break
        
        if not corrupt:
            score = 0
            for c in reversed(stack):
                score = score*5 + score_incomplete[c]
            scores_incomplete.append(score)

    return sum_corrupt, median(scores_incomplete)

raw = read_input(2021, 10)
lines = raw.split()
result1, result2 = puzzles(lines)

print(f"Puzzle 1: {result1}")
print(f"Puzzle 2: {result2}")