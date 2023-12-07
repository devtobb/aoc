#!/usr/bin/env python3

from collections import defaultdict
from pprint import pprint

from tools import read_input

def all_path(path, graph, max_visit):
    vert_cur = path[-1]
    if vert_cur == 'end':
        return [path]
    vert_next = graph[vert_cur]
    
    explore = []
    for v in vert_next:
        if v.upper()==v:
            explore.append(v)
            continue
        if v == 'start':
            continue
        if v == 'end':
            explore.append(v)
            continue
        if max([path.count(v) for v in path if v.upper()!=v]) < max_visit or v not in path:
            explore.append(v)

    ret = []
    for v in explore:
        rest = all_path(path + [v], graph, max_visit)
        for r in rest:
            if r: ret.append(r)
    
    return ret

def puzzle1(graph):
    return len(all_path(['start'], graph, 1))

def puzzle2(graph):
    return len(all_path(['start'], graph, 2))

raw = read_input(2021, 12)
edges = [l.split('-') for l in raw.split()]
graph = defaultdict(list)

for v1, v2 in edges:
    graph[v1].append(v2)
    graph[v2].append(v1)


print(f"\033[97m★\033[00m {puzzle1(graph)}")
print(f"\033[93m★\033[00m {puzzle2(graph)}")