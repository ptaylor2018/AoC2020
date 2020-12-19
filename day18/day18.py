import typing
import math


def part1():
    input_raw = []
    with open("input_day18.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())

    sum = 0
    for line in input_cleaned:
        # print(line)
        ans = compute_answer(line)
        # print(ans)
        sum += ans
    return sum


def compute_answer(line: str) -> int:
    if contains_no_parens(line):
        # print(line)
        return do_math(line)
    else:
        prefix, seg, postfix = sep_paren_seg(line)
        return compute_answer(prefix + str(compute_answer(seg)) + postfix)


def contains_no_parens(line: str) -> bool:
    for char in line:
        if char == "(" or char == ")":
            return False
    return True


def do_math(line: str) -> int:
    basket = []
    operator = ""
    bits = line.split(" ")
    for bit in bits:
        if bit.isdigit():
            if not basket:
                basket.append(int(bit))
            else:
                if operator == "*":
                    basket[0] = basket[0] * int(bit)
                if operator == "+":
                    basket[0] = basket[0] + int(bit)
        else:
            operator = bit
    return basket[0]


def sep_paren_seg(line: str) -> [str, str, str]:
    open_loc = 0
    for i in range(len(line)):
        if line[i] == "(":
            open_loc = i
            break

    close_loc = 0
    level_count = 0
    for i in range(open_loc, len(line)):
        if line[i] == "(":
            level_count += 1
        if line[i] == ")":
            level_count -= 1
            if level_count == 0:
                close_loc = i
                break

    prefix = line[0:open_loc]
    seg = line[open_loc + 1 : close_loc]
    postfix = line[close_loc + 1 :]
    # print([prefix, seg, postfix])
    return [prefix, seg, postfix]


print(part1())


def part2():
    input_raw = []
    with open("input_day18.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())

    sum = 0
    for line in input_cleaned:
        # print(line)
        ans = compute_answer_2(line)
        # print(ans)
        sum += ans
    return sum


def compute_answer_2(line: str) -> int:
    if contains_no_parens(line):
        # print(line)
        return do_math_2(line)
    else:
        prefix, seg, postfix = sep_paren_seg(line)
        return compute_answer_2(prefix + str(compute_answer_2(seg)) + postfix)


def do_math_2(line: str) -> int:
    basket = []
    operator = ""
    bits = line.split(" ")
    for bit in bits:
        if bit.isdigit():
            if not basket:
                basket.append(int(bit))
            else:
                if operator == "*":
                    basket.append(int(bit))
                if operator == "+":
                    basket[-1] = basket[-1] + int(bit)
        else:
            operator = bit
    return math.prod(basket)


print(part2())