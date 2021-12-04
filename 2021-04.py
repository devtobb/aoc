#!/usr/bin/env python3

import numpy as np 

from aoc import read_input

def is_bingo(drawn):
    return np.any([np.any(np.all(drawn, axis=ax)) for ax in (1, 2)])

def winning_boards(drawn):
    b1, _ = np.where(np.all(drawn, axis=1))
    b2, _ = np.where(np.all(drawn, axis=2))
    boards = np.concatenate((b1, b2))
    return np.unique(boards)

def puzzle1(nums, boards):
    drawn = np.zeros(boards.shape)
    while not is_bingo(drawn):
        num = nums.pop(0)
        drawn[np.where(boards==num)] = True

    winner, *_ = winning_boards(drawn)
    return np.sum(boards[winner, np.logical_not(drawn[winner])]) * num


def puzzle2(nums, boards):
    drawn = np.zeros(boards.shape)
    remaining = list(range(len(boards)))
    winners = []
    while len(winners) < len(boards):
        num = nums.pop(0)
        drawn[np.where(boards==num)] = True
        winners = winning_boards(drawn)
        if len(winners) < len(boards):
            remaining = [n for n in range(len(boards)) if n not in winners]

    last, *_ = remaining

    return np.sum(boards[last, np.logical_not(drawn[last])]) * num

raw = read_input(2021, 4)[:-1]
nums, *boards = raw[:-1].split("\n\n")
nums = list(map(int, nums.split(",")))
boards = np.array([[list(map(int, l.split())) for l in b.split('\n')] for b in boards])


print(f"Puzzle 1: {puzzle1(nums.copy(), boards)}")
print(f"Puzzle 2: {puzzle2(nums.copy(), boards)}")