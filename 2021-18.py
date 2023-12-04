#!/usr/bin/env python3

from itertools import product
import re

from aoc import read_input

class SnailNumber:
    def __init__(self, num):
        self.num = num

    def reduce(self):
        change = True
        while change:
            change = False
            if self.explode():
                change = True
                continue
            if self.split():
                change = True
                continue

    def explode(self):
        depth = 0
        for n, char in enumerate(self.num):
            if char == "[": depth+=1
            if char == "]": depth-=1
            if depth == 5:
                
                start = n
                end = self.num.index("]", start)
                left, right = re.findall(r'\d+', self.num[start:end])
                
                lstr = self.num[:start]
                rstr = self.num[end+1:]
                
                numbers_left = list(re.finditer(r'\d+', lstr))
                numbers_right= list(re.finditer(r'\d+', rstr))

                if numbers_left:
                    m = numbers_left[-1]
                    numleft = int(m.group()) + int(left)
                    lstart, lend = m.span()
                    lstr = lstr[:lstart] + str(numleft) + lstr[lend:]

                if numbers_right:
                    m, *_ = numbers_right
                    numright = int(m.group()) + int(right)
                    rstart, rend = m.span()
                    rstr = rstr[:rstart] + str(numright) + rstr[rend:]


                self.num =  lstr + "0" + rstr
                return True
        return False
    
    def split(self):
        number_matches = list(re.finditer(r"\d\d+", self.num))
        if(number_matches):
            m, *_ = number_matches
            start, end = m.span()
            n = int(m.group())
            self.num = self.num[:start] + f"[{n//2},{n//2 + n%2}]" + self.num[end:]
            return True
        return False
    
    def magnitude(pair):
        if type(pair) == int:
            return pair

        left, right = pair
        return 3*SnailNumber.magnitude(left) + 2*SnailNumber.magnitude(right)

    def __add__(self, other):
        new = SnailNumber(f"[{self.num},{other.num}]")
        new.reduce()
        return new

    def __abs__(self):
        pair = eval(self.num)
        return SnailNumber.magnitude(pair)

    def __str__(self):
        return f"{self.num}"

    def __repr__(self):
        return f"<SnailNumber: {str(self)}>"

def puzzle1(numbers):
    first, *rest = numbers
    return abs(sum(rest, first))

def puzzle2(numbers):
    return max(abs(a + b) for a, b in product(numbers, numbers))

raw = read_input(2021, 18)
numbers = list(map(SnailNumber, raw.splitlines()))

print(f"\033[97m★\033[00m {puzzle1(numbers)}")
print(f"\033[93m★\033[00m {puzzle2(numbers)}")