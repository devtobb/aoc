#!/usr/bin/env python3

from itertools import accumulate
import numpy as np 

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

from aoc import read_input

def raw_to_coord_delta(raw):
    direction, *_ = raw
    raw = raw.translate({82:'', 85:'', 76:'-', 68:'-'})
    delta = int(raw)

    if direction in "RL":
        return np.array((delta, 0))
    else:
        return np.array((0, delta))


wire1, wire2 = [path.split(',') for path in read_input(2019, 3).split()]

wire1 = np.stack([(0, 0)] + list(accumulate(map(raw_to_coord_delta, wire1))))
wire2 = np.stack([(0, 0)] + list(accumulate(map(raw_to_coord_delta, wire2))))

plt.plot(wire1[:, 0], wire1[:, 1], 'g', wire2[:, 0], wire2[:, 1], 'r')

plt.show()