#!/usr/bin/env python3

from math import prod

import numpy as np

from tools import *

def puzzle1(raw):
    *nums, ops = raw.split("\n")[:-1]
    nums = np.array([list(map(int, row.split())) for row in nums])
    ops = np.array(ops.split())
    sums = np.sum(nums[:, ops=="+"], axis=0)
    prods = np.prod(nums[:, ops=="*"], axis=0)
    return sum(sums) + sum(prods)

def puzzle2(raw):
    *lines, ops = raw.split("\n")[:-1]
    cols = [i for i, op in enumerate(ops) if op!=" "]
    result = 0
    for s, e in zip(cols, cols[1:] + [len(lines[0])+1]):
        nums = []
        for n in range(s, e - 1):
            nums.append(int(''.join(line[n] for line in lines)))
        result += sum(nums) if ops[s] == "+" else prod(nums)
    return result
    
raw = read_input(2025, 6)

print(f"\033[97m★\033[00m {puzzle1(raw)}")
print(f"\033[93m★\033[00m {puzzle2(raw)}")