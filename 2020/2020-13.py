#!/usr/bin/env python3

from math import prod, ceil
from functools import reduce
from tools import read_input

def modmultinv(a, m):
    t, next_t = 0, 1
    r, next_r = m, a

    while next_r != 0:
        q = r // next_r if r > 0 else ceil(r / next_r)
        t, next_t = next_t, t - q * next_t
        r, next_r = next_r, r- q * next_r
        print(f"q_n={q}, t_n={t}, t_n+1={next_t}, r_n={r}, r_n+1={next_r}")

    if r > 1:
        raise Exception(f"{a} not invertible on Z_{m}")

    if t < 0: t+=m

    return t

def f(bus1, bus2):
    a_1, m_1 = bus1
    a_2, m_2 = bus2

    return (a_1 * m_2 * modmultinv(m_2, m_1) +
            a_2 * m_1 * modmultinv(m_1, m_2)) % (m_1 * m_2), m_1*m_2

def puzzle1(departure, busse):
    earliest = min([(bus, bus - departure % bus) for _, bus in busses], key=lambda b: b[1])
    return prod(earliest)

def puzzle2(busses):
    return reduce(f, busses)

raw = read_input(2020, 13)
departure, busses = raw.split()
departure = int(departure)
busses = [(-pos, int(bus)) for pos, bus in enumerate(busses.split(',')) if bus.isdigit()]

print("Puzzle 1: {}".format(puzzle1(departure, busses)))
print("Puzzle 2: {}".format(puzzle2(busses)))