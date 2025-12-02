
from itertools import accumulate

from tools import read_input, blist

raw = read_input(2025, 1)
rotations = blist(raw.replace("R", "+").replace("L", "-").split()) >> int
positions = blist(accumulate([50] + rotations)) >> (lambda x:x%100)
puzzle1 = positions.count(0)
puzzle2 = sum(abs((p+r)//100) - (1 if (p==0 and r<0) else 0) + (1 if ((p+r)%100==0 and r<0) else 0) for p, r in zip(positions, rotations))

print(f"\033[97m★\033[00m {puzzle1}")
print(f"\033[93m★\033[00m {puzzle2}")