#!/usr/bin/env python3

from aoc import read_input

vsum = 0

def packet_type(bits):
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    bits = bits[6:]
    global vsum
    vsum += version
    print(f"Packet: V={version}, T={type_id}")
    # print(f"Bits: {bits}")
    return version, type_id, bits

def literal(bits):
    n = bits[1:5]
    first, *_ = bits
    bits = bits[5:]
    while first == '1':
        first, *_ = bits
        n += bits[1:5]
        bits = bits[5:]
    return int(n, 2), bits

def operator(bits):
    # print(f"Bits: {bits}")
    ltype = bits[0]
    bits = bits[1:]
    if ltype == '0':
        l = int(bits[:15], 2)
        subbits = bits[15:15+l]
        bits = bits[15+l:]
        print(f"Sub-Packet by len: {l}")
        while subbits:
            subbits = parse(subbits)
    else:
        n = int(bits[:11], 2)
        bits = bits[11:]
        print(f"Sub-Packet by n: {n}")
        bits = parse_n(bits, n)
    return bits

def parse(bits):
    version, type_id, bits = packet_type(bits)
    if type_id == 4:
        n, bits = literal(bits)
        print(f"Literal: {n}")
    else:
        bits = operator(bits)
    return bits

def parse_n(bits, n):
    for _ in range(n):
        bits = parse(bits)
    return bits


def puzzle1(bits):
    # vsum = 0
    while bits:
        try:
            bits = parse(bits)
        except:
            break
    return vsum

def puzzle2():
    pass

raw = read_input(2021, 16)
bits = format(int(raw, 16), "0"+str(len(raw.strip())*4)+"b")
bitsn = list(map(int, list(bits)))

print(f"\033[97m★\033[00m {puzzle1(bits)}")
print(f"\033[93m★\033[00m {puzzle2()}")