from itertools import chain, repeat

from aoc import read_input

def instruction(code, instr_ptr, accu):
    operation, argument = code
    
    if operation == "nop":
        return instr_ptr + 1, accu
    elif operation == "jmp":
        return instr_ptr + argument, accu
    elif operation == "acc":
        return instr_ptr + 1,  accu + argument

    raise RuntimeError("Unsupported operation: {}".format(operation))

def run(code):
    n_instr = len(code)
    executed = [0]*n_instr
    instr_ptr = accu = 0
    
    while executed[instr_ptr] == 0:
        executed[instr_ptr] = 1
        instr_ptr, accu = instruction(code[instr_ptr], instr_ptr, accu)
        # terminates
        if instr_ptr == n_instr:
            return accu, True
        # segfaults
        if instr_ptr > n_instr or instr_ptr < 0:
            return accu, False

    return accu, False

def puzzle1(code):
    accu, _ = run(code)    
    return accu

def puzzle2(code):
    terminates = False
    jmps = (idx for idx in range(len(code)) if code[idx][0]=='jmp')
    nops = (idx for idx in range(len(code)) if code[idx][0]=='nop')
    for new_op, idx in chain(zip(repeat("nop"), jmps), zip(repeat("jmp"), nops)):
        op, arg = code[idx]
        code[idx] = (new_op, arg)
        accu, terminates = run(code)
        code[idx] = (op, arg)
        if terminates:      
            return accu


code = [line.split() for line in read_input(2020, 8).split('\n')[:-1]]
code = [(op, int(arg)) for (op, arg) in code]

print("Puzzle 1: {}".format(puzzle1(code)))
print("Puzzle 2: {}".format(puzzle2(code)))