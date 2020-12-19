#!/usr/bin/env python3

from math import ceil
import re

from aoc import read_input

def rules_to_regex(rules):
    expanded = True
    while expanded:
        expanded = False
        for rule in rules:
            if re.match(r'.*\d+.*', rules[rule]):
                rules[rule] = re.sub(
                    r'\d+', 
                    lambda m: '('+rules[m.group()]+')', 
                    rules[rule])
                expanded = True

    rules = {rule:'('+rules[rule].translate({34:'',32:''})+')' for rule in rules}

    return rules

def min_chars_from_rule(rule, rules):
    if not re.match(r'.*\d+.*', rules[rule]):
        return 1
    
    alternatives = rules[rule].split('|')

    sums = []
    for alternative in alternatives:
        sums.append(sum(min_chars_from_rule(rule, rules) for rule in re.findall(r'\d+', alternative)))
    
    return min(sums)

def count_matches(rules, messages):
    rules = rules_to_regex(rules.copy())
    return sum(re.fullmatch(rules['0'], message) is not None for message in messages)

def puzzle1(rules, messages):
    return count_matches(rules, messages)

def puzzle2(rules, messages):
    max_word_len = max(len(m) for m in messages)
    max_rec_depth = max_word_len // (min_chars_from_rule('42', rules) + min_chars_from_rule('31', rules)) + 1

    rules['8'] = '(42)+'
    rules['11'] = '|'.join('(42)'*n+'(31)'*n for n in range(1, max_rec_depth))
    return count_matches(rules, messages)


rules, messages = read_input(2020, 19).split('\n\n')
rules =  dict([rule.split(': ') for rule in rules.split('\n')])
messages = messages.split()

print(f"Puzzle 1: {puzzle1(rules, messages)}")
print(f"Puzzle 2: {puzzle2(rules, messages)}")