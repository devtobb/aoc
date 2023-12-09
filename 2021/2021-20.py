#!/usr/bin/env python3

import numpy as np
from scipy.signal import convolve2d

from tools import *

def enhance(img, enh):
    mask = np.array([1<<n for n in range(9)]).reshape((3,3))
    img = convolve2d(img, mask)
    for idx, val in enumerate(enh):
        img[img==idx] = val
    return img

def total_lit(img, enh, run_n_times=2):
    pad = run_n_times*2
    img = np.pad(img, pad)
    for _ in range(run_n_times):
        img = enhance(img, enh)
    result = img[pad:-pad, pad:-pad]
    return np.sum(result)

def line_to_int(line):
    return [0 if c=='.' else 1 for c in line]

def puzzle1(img, enh):
    return total_lit(img, enh)

def puzzle2(img, enh):
    return total_lit(img, enh, run_n_times=50)

raw = read_input(2021, 20)
enh, img = raw.split('\n\n')
enh = np.array(line_to_int(enh))
img = np.array(list(map(line_to_int, img.splitlines())))

print(f"\033[97m★\033[00m {puzzle1(img, enh)}")
print(f"\033[93m★\033[00m {puzzle2(img, enh)}")