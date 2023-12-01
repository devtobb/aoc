#!/usr/bin/env python3

import numpy as np 

from aoc import read_input

def winning_boards(drawn):
    bvert, _ = np.where(np.all(drawn, axis=1))
    bhor, _ = np.where(np.all(drawn, axis=2))

    boards = np.concatenate((bvert, bhor))
    return np.unique(boards)

def play_until(nums, boards, until):
    drawn = np.zeros(boards.shape)
    winners = {}
    while until(winners, boards):
        num = nums.pop(0)
        drawn[np.where(boards==num)] = True
        winners_cur = winning_boards(drawn)
        for winner in winners_cur:
            winners[winner] = None

    return list(winners.keys()), drawn, num

def score(winner, boards, drawn, num):
    return np.sum(boards[winner, np.logical_not(drawn[winner])]) * num

def puzzle1(nums, boards):
    winners, drawn, num = play_until(nums, boards, lambda w, b: len(w)==0)
    winner, *_ = winners

    return score(winner, boards, drawn, num)

def puzzle2(nums, boards):
    winners, drawn, num = play_until(nums, boards, lambda w, b: len(w)<len(b))
    *_, winner  = winners

    return score(winner, boards, drawn, num)

raw = read_input(2021, 4)[:-1]
nums, *boards = raw.split("\n\n")
nums = list(map(int, nums.split(",")))
boards = np.array([[list(map(int, l.split())) for l in b.split('\n')] for b in boards])


print(f"Puzzle 1: {puzzle1(nums.copy(), boards)}")
print(f"Puzzle 2: {puzzle2(nums.copy(), boards)}")