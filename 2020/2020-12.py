#!/usr/bin/env python3

from tools import read_input
from collections import defaultdict
from functools import reduce
from numpy import eye, dot

sgn = dict(N=1j,S=-1j,E=1,W=-1,R=-1,L=1,F=1)
pos = [defaultdict(lambda:(2,0),R=(1,1),L=(1,1),F=(1,0)),
       defaultdict(lambda:(2,1),R=(1,1),L=(1,1),F=(1,0))]
fnc = defaultdict(lambda:lambda s,m:m*s, 
            R=lambda s,m:1j**(s*m/90), L=lambda s,m:1j**(s*m/90))

def afftrans(i, m, puzzle):
    mat = eye(3, dtype=complex)
    mat[pos[puzzle][i]]=fnc[i](sgn[i], m)
    return mat

def transform(instr, start, puzzle):
    dest, *_= dot(start, reduce(dot, (afftrans(i,m,puzzle) for (i,m) in instr)))
    return  int(abs(dest.imag) + abs(dest.real))

def puzzle1(instr):
    return transform(instr, [0,1,1], 0)

def puzzle2(instr):
    return transform(instr, [0,10+1j,1], 1)

instr = [(row[0], int(row[1:])) for row in read_input(2020, 12).split()]

print("Puzzle 1: {}".format(puzzle1(instr)))
print("Puzzle 2: {}".format(puzzle2(instr)))