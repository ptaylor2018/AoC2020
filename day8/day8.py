def part1():
    input_raw = []
    with open("input_day8.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip().split())

    executed_lines = [0 for i in range(len(input_cleaned))]
    line_num = 0
    acc = 0
    no_double = True
    while no_double:
        instr = input_cleaned[line_num][0]
        amt = int(input_cleaned[line_num][1])
        executed_lines[line_num] += 1
        if executed_lines[line_num] > 1:
            return acc
            no_double = False  # this is really just future proof for part 2

        if instr == "acc":
            acc += amt
            line_num += 1
        elif instr == "jmp":
            line_num += amt
        elif instr == "nop":
            line_num += 1


print(part1())

import copy


def part2():
    input_raw = []
    with open("input_day8.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip().split())

    for i in range(len(input_cleaned)):
        instr = input_cleaned[i][0]
        input_to_check = copy.deepcopy(input_cleaned)
        if instr == "jmp":
            input_to_check[i][0] = "nop"
        elif instr == "nop":
            input_to_check[i][0] = "jmp"
        result = check_program(input_to_check)
        if result != False:
            return result


def check_program(input_cleaned):
    executed_lines = [0 for i in range(len(input_cleaned))]
    line_num = 0
    acc = 0
    no_double = True
    while no_double:
        if line_num == len(input_cleaned):
            return acc
        instr = input_cleaned[line_num][0]
        amt = int(input_cleaned[line_num][1])
        executed_lines[line_num] += 1
        if executed_lines[line_num] > 1:
            return False
            no_double = False

        if instr == "acc":
            acc += amt
            line_num += 1
        elif instr == "jmp":
            line_num += amt
        elif instr == "nop":
            line_num += 1


print(part2())
