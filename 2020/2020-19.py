#!/usr/bin/env python3

import re

from tools import read_input

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

def min_chars(rule, rules):
    if not re.match(r'.*\d+.*', rules[rule]):
        return 1
    alts = rules[rule].split('|')
    return min(sum(min_chars(r, rules) for r in re.findall(r'\d+', a)) for a in alts)
    

def count_matches(rules, messages):
    rules = rules_to_regex(rules.copy())
    pattern = re.compile(rules['0'])
    return sum(pattern.fullmatch(message) is not None for message in messages)

def puzzle1(rules, messages):
    return count_matches(rules, messages)

def puzzle2(rules, messages):
    max_msg_len = max(len(m) for m in messages)
    max_rec_depth = max_msg_len // (min_chars('42', rules) + min_chars('31', rules))

    rules['8'] = '(42)+'
    rules['11'] = '|'.join('(42)'*n+'(31)'*n for n in range(1, max_rec_depth+1))
    return count_matches(rules, messages)


rules, messages = read_input(2020, 19).split('\n\n')
rules =  dict([rule.split(': ') for rule in rules.split('\n')])
messages = messages.split()

print(f"Puzzle 1: {puzzle1(rules, messages)}")
print(f"Puzzle 2: {puzzle2(rules, messages)}")