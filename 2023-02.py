#!/usr/bin/env python3

from functools import reduce
from math import prod
import re

from aoc import read_input

colors = 'rgb'

def turn(token):
    n, color = token.split()
    return int(n), color

def game(line):
    return tuple(map(turn, re.findall(r'\d+ \w', line)))

def is_valid_turn(turn):
    n, color = turn
    return n < colors.index(color) + 13

def is_valid_game(game):
    _, game = game
    return all(map(is_valid_turn, game))

def score(game):
    score, _ = game
    return score

def power(game):
    return prod(max(map(score, filter(lambda t: t[1]==c, game))) for c in colors)

def puzzle1(games):
    return sum(map(score, filter(is_valid_game, enumerate(games, 1))))

def puzzle2(games):
    return sum(map(power, games))

lines = read_input(2023, 2).splitlines()
games = tuple(map(game, lines))

print(f"\033[97m★\033[00m {puzzle1(games)}")
print(f"\033[93m★\033[00m {puzzle2(games)}")