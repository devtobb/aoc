#!/usr/bin/env python3

from functools import reduce
from math import prod

from aoc import read_input

colors = ('red', 'green', 'blue')

def game(line):
    game, turns = line.split(":")
    _, gid = game.split()
    turns = [{color.split()[1]:int(color.split()[0]) for color in turn.split(',')} for turn in turns.split(';')]
    return dict(gid=int(gid), turns=turns)

def is_valid_turn(turn):
    return all(turn.get(color, 0)<n for n, color in enumerate(colors, 13))

def is_valid_game(game):
    return all(map(is_valid_turn, game['turns']))

def power(game):
    return prod(reduce(max, (turn.get(color, 0) for turn in game['turns'])) for color in colors)

def puzzle1(games):
    return sum(map(lambda g: g['gid'], filter(is_valid_game, games)))

def puzzle2(games):
    return sum(map(power, games))

lines = read_input(2023, 2).splitlines()
games = list(map(game, lines))

print(f"\033[97m★\033[00m {puzzle1(games)}")
print(f"\033[93m★\033[00m {puzzle2(games)}")