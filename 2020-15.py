#!/usr/bin/env python3

from aoc import read_input
from collections import defaultdict


def ith_number(nums, i):
    num = nums[-1]
    last_spoken = defaultdict(lambda:(-1, -1), {num:(n, -1) for n,num in enumerate(nums)})
    for n in range(len(nums), i):
        last, prev = last_spoken[num]
        if last > -1 and prev > -1:
            num = last - prev
        else:
            num = 0

        last, prev = last_spoken[num]
        last_spoken[num] = (n, last)

    return num

def puzzle1(nums):
    return ith_number(nums, 2020)

def puzzle2():
    return ith_number(nums, 30000000)

raw = read_input(2020, 15)
nums = list(map(int, raw.split(',')))

print("Puzzle 1: {}".format(puzzle1(nums)))
print("Puzzle 2: {}".format(puzzle2()))