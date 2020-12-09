import copy


def part1():
    input = []
    with open("input_day9.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input.append(line)
    input_cleaned = []
    for item in input:
        input_cleaned.append(int(item.rstrip()))
    # print(input_cleaned)

    chunk_size = 25
    i = chunk_size
    while i < len(input_cleaned):
        goal_sum = input_cleaned[i]
        ans = find_pair(input_cleaned, i, chunk_size, goal_sum)
        if ans is False:
            return [goal_sum, i]
        i += 1


def find_pair(input_cleaned, i, chunk_size, goal_sum):
    for j in range(i - chunk_size, i):
        input_trimmed = copy.deepcopy(input_cleaned[i - chunk_size : i])
        currently_checking = input_cleaned[j]
        wanted_diff = goal_sum - currently_checking
        if wanted_diff in input_trimmed:
            return [wanted_diff, currently_checking]
    return False


print(part1())


def part2():
    input = []
    with open("input_day9.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input.append(line)
    input_cleaned = []
    for item in input:
        input_cleaned.append(int(item.rstrip()))
    # print(input_cleaned)

    wanted_sum = input_cleaned[633]

    list_length = 2

    for list_length in range(2, len(input_cleaned)):
        start_index = 0
        end_index = list_length
        while end_index < len(input_cleaned):
            check_segment = input_cleaned[start_index:end_index]
            if wanted_sum == sum(check_segment):
                print(check_segment)
                return min(check_segment) + max(check_segment)
            start_index += 1
            end_index += 1


print(part2())