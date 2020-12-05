from aoc import read_input

def puzzle1(entries):
    s = 0
    target = 2020
    n = len(entries)
    upper = n - 1
    lower = 0
    while s!=target:
        s = entries[lower] + entries[upper]
        if s > target:
            upper -= 1
        if s < target:
            lower += 1
            upper = n - 1

    return entries[upper] * entries[lower]

def puzzle2(entries):
    s = 0
    target = 2020
    n = len(entries)
    
    upper = n - 1
    lower1 = 0
    
    while s!=target:
        for lower2 in range(lower1 + 1, upper):
            s = entries[lower1] + entries[lower2] + entries[upper]
            if s == target:
                break
        if s > target:
            upper -= 1
        if s < target:
            lower1 += 1
            upper = n - 1

    return entries[upper] * entries[lower1] * entries[lower2]


entries = sorted(map(int, read_input(__file__).split()))

print("Puzzle 1: {}".format(puzzle1(entries)))
print("Puzzle 2: {}".format(puzzle2(entries)))
