#!/usr/bin/env python3

from tools import *

# tilt to east
def tilt(board):
    newboard = []
    for line in board:
        newline = ''
        unknown = line
        while len(unknown) > 0:
            if unknown[0] == '#':
                unknown = unknown[1:]
                newline = newline + '#'
            else:
                right = unknown.find('#')
                right = right if right > -1 else len(unknown)
                stones = unknown[:right].count('O')
                dots = unknown[:right].count('.')
                assert stones + dots == right
                newline = newline + 'O'*stones + '.'*dots
                unknown = unknown[right:]
        newboard.append(newline)
    return tuple(newboard)
        
def total_load(board):
    height = len(board)
    return sum(line.count('O') * (height - n) for n, line in enumerate(board))

# clockwise
def rot90(board):
    return tuple(''.join(reversed(l)) for l in zip(*board))

def puzzle1(board):
    return(total_load(rot90(tilt(rot90(rot90(rot90((board))))))))

def puzzle2(board):
    # turn north toward west first
    board = rot90(rot90(rot90(board)))

    n = 0
    turns = dict()
    total = 1_000_000_000
    while n < total:
        if board in turns:
            period = n - turns[board]
            n = total - (total - n) % period
        else:
            turns[board] = n

        for c in range(4):
            board = rot90(tilt(board))
        
        n += 1
    board = rot90(board)

    
    return total_load(board)

raw = read_input(2023, 14, '')
board = tuple(raw.splitlines())


print(f"\033[97m★\033[00m {puzzle1(board)}")
print(f"\033[93m★\033[00m {puzzle2(board)}")