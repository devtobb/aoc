from aoc import read_input

def puzzle1(nums):
    invalid, *_ = [n for n in range(25, len(nums)) 
                    if nums[n] not in 
                        (nums[a]+nums[b] 
                            for a in range(n-25, n) 
                                for b in range(a+1, n))]                                                                                                
    return nums[invalid]

def puzzle2(nums, invalid):
    lower = upper = 0
    s = nums[lower]
    while s != invalid:
        upper += 1
        s += nums[upper]
        if s > invalid:
            lower += 1
            upper = lower
            s = nums[lower]
    return min(nums[lower:upper+1]) + max(nums[lower:upper+1])

raw = read_input(2020, 9)
nums = list(map(int, raw.split()))

print("Puzzle 1: {}".format(invalid:=puzzle1(nums)))
print("Puzzle 2: {}".format(puzzle2(nums, invalid)))