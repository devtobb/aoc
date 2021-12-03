#!/usr/bin/env python3
import numpy as np

from aoc import read_input

def freqs(raw):
    ret = np.zeros((12, 2))
    for n in range(12):
        _, freq = np.unique(raw[:, n], return_counts=True)
        ret[n, :] = freq
    return ret

def most_common(raw):
    freq = freqs(raw)
    freq[:,1] = freq[:,1] + (freq[:,0]==freq[:,1])
    return np.argmax(freq, axis=1)

def least_common(raw):
    freq = freqs(raw)
    freq[:,0] = freq[:,0] - (freq[:,0]==freq[:,1])
    return np.argmin(freq, axis=1)

def arr2bin(arr):
    return int("".join(map(str, arr)), 2)

def puzzle1(raw):
    return arr2bin(most_common(raw)) * arr2bin(least_common(raw))

def puzzle2(raw):
    ox = np.copy(raw)
    n = 0
    while len(ox) > 1:
        mc = most_common(ox)
        ox = ox[ox[:, n]==mc[n], :]
        n += 1

    co = np.copy(raw)
    n = 0
    while len(co) > 1:
        lc = least_common(co)
        co = co[co[:, n]==lc[n], :]
        n += 1

    return arr2bin(ox[0]) * arr2bin(co[0])

raw = read_input(2021, 3)
raw = np.array([[int(e) for e in l] for l in raw.split()])

print(f"Puzzle 1: {puzzle1(raw)}")
print(f"Puzzle 2: {puzzle2(raw)}")