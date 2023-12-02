#!/usr/bin/env python3

from collections import namedtuple
from functools import reduce
from math import prod
import re

from aoc import read_input

colors = 'rgb'
Turn = namedtuple('Turn', 'n color')
Game = namedtuple('Game', 'id turns')

def turn(token):
    n, color = token.split()
    return Turn(int(n), color)

def game(line):
    gid, = re.match('Game (\d+):', line).groups()
    return Game(int(gid), tuple(map(turn, re.findall(r'\d+ \w', line))))

def is_valid_turn(turn):
    return turn.n < colors.index(turn.color) + 13

def is_valid_game(game):
    return all(map(is_valid_turn, game.turns))

def power(game):
    return prod(max((turn.n for turn in game.turns if turn.color==color), default=0) for color in colors)

def puzzle1(games):
    return sum(game.id for game in filter(is_valid_game, games))

def puzzle2(games):
    return sum(map(power, games))

lines = read_input(2023, 2).splitlines()
games = tuple(map(game, lines))

print(f"\033[97m★\033[00m {puzzle1(games)}")
print(f"\033[93m★\033[00m {puzzle2(games)}")