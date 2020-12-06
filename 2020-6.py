from functools import reduce

from aoc import read_input

def group_reduce(groups, func):
    return sum(len(reduce(func, group)) for group in groups)

def puzzle1(groups):
    return group_reduce(groups, lambda a,b:a|b)

def puzzle2(groups):
    return group_reduce(groups, lambda a,b:a&b)

raw = read_input(__file__).split('\n\n')
groups = [list(map(lambda a:set(a), group.split())) for group in raw]

print("Puzzle 1: {}".format(puzzle1(groups)))
print("Puzzle 2: {}".format(puzzle2(groups)))

