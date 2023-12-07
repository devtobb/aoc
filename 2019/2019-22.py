#!/usr/bin/env python3

from tools import read_input

def modmultinv(a, m):
    t, next_t = 0, 1
    r, next_r = m, a

    while next_r != 0:
        q = r // next_r if r > 0 else ceil(r / next_r)
        t, next_t = next_t, t - q * next_t
        r, next_r = next_r, r- q * next_r
        # print(f"q_n={q}, t_n={t}, t_n+1={next_t}, r_n={r}, r_n+1={next_r}")

    if r > 1:
        raise Exception(f"{a} not invertible on Z_{m}")

    if t < 0: t+=m

    return t

def f(a, b):
    a_1, m_1 = a
    a_2, m_2 = b

    return (a_1 * m_2 * modmultinv(m_2, m_1) +
            a_2 * m_1 * modmultinv(m_1, m_2)) % (m_1 * m_2)

def deal_new(stack):
    return stack[::-1]

def cut(stack, n):
    return stack[n:] + stack[:n]

def deal_inc_idx(idx, i, l):
    return f((0, l), (idx, i)) % l

def deal_inc(stack, i):
    # r1 =  [stack[((-n)*(i))%len(stack)] for n in range(len(stack))]
    l = len(stack)
    ret = [None] * l
    idx = [(n*i)%l for n in range(l)]
    for s in range(l):
        ret[idx[s]] = stack[s]
    # if r1 != ret:
    #     print(f'unequal inc({i}): {stack}, {r1}, {ret}')
    return tuple(ret)

def run(instr, stack):
    for i in instr:
        if i.startswith("deal into"):
            stack = deal_new(stack)
        elif i.startswith("deal"):
            _, _, _, n = i.split()
            stack = deal_inc(stack, int(n))
        else:
            _, n = i.split()
            stack = cut(stack, int(n))
    return stack

def puzzle1(instr):
    stack = tuple(range(10007))
    stack = run(instr, stack)
    pos, *_ = [n for (n, c) in enumerate(stack) if c==2019]
    return(pos)

def puzzle2():
    stack = tuple(range(119315717514047))
    for _ in range(101741582076661):
        stack = run(stack)

    pos, *_ = [n for (n, c) in enumerate(stack) if c==2019]
    return(pos)


raw = read_input(2019, 22)
instr = tuple(raw.split('\n')[:-1])

print(f"Puzzle 1: {puzzle1(instr)}")
print(f"Puzzle 2: {puzzle2()}")