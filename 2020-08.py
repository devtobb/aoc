from aoc import read_input

def instruction(code):
    operation, argument = code.split()
    argument = int(argument)
    
    def nop(instr_ptr, accu):
        return instr_ptr + 1, accu
    
    def jmp(instr_ptr, accu):
        return instr_ptr + argument, accu

    def acc(instr_ptr, accu):
        return instr_ptr + 1,  accu + argument

    return dict(
        nop = nop,
        jmp = jmp,
        acc = acc
    ).get(operation)

def run(code):
    n_instr = len(code)
    executed = [0]*n_instr
    instr_ptr = accu = 0
    
    while executed[instr_ptr] == 0:
        # terminates
        if instr_ptr == n_instr:
            return accu, True
        # segfaults
        if instr_ptr > n_instr:
            return accu, False
        executed[instr_ptr] = 1
        instr_ptr, accu = code[instr_ptr](instr_ptr, accu)
    
    return accu, False

def puzzle1(code):
    accu, _ = run(code)    
    return accu

def puzzle2(code):
    pass


code = list(map(instruction, read_input(2020, 8).split('\n')[:-1]))

print("Puzzle 1: {}".format(puzzle1(code)))
print("Puzzle 2: {}".format(puzzle2(code)))