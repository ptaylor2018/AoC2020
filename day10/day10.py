
def part1():
    input = []
    with open("input_day10.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input.append(line)
    input_cleaned = []
    for item in input:
        input_cleaned.append(int(item.rstrip()))
    input_cleaned = sorted(input_cleaned)
    # print(input_cleaned)

    current_joltage = 0
    diffs = [0,0,0]
    for num in input_cleaned:
        diff = num - current_joltage
        diffs[diff - 1] +=1
        current_joltage = num
    diffs[2] += 1
    return diffs[0] * diffs[2]

print(part1())

def part2():
    input = []
    with open("input_day10.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input.append(line)
    input_cleaned = []
    for item in input:
        input_cleaned.append(int(item.rstrip()))
    input_cleaned = sorted(input_cleaned)
    # print(input_cleaned)

    max_joltage = input_cleaned[-1] + 3
    starting_list = [0]+ input_cleaned + [max_joltage]
    #return len(check_path(max_joltage, starting_list[:], [],[max_joltage][:]))
    known_combos = {
        0:1
    }
    for joltage in starting_list:
        known_combos[joltage] = check_path_better(joltage, known_combos, starting_list)

    return known_combos[max_joltage]
    




# return number of combos that can be made from that joltage
def check_path_better(joltage, known_combos, input):
    if joltage not in input:
        return 0
    if joltage < 0:
        return 0
    if joltage in known_combos:
        return known_combos[joltage]
    else:
        return check_path_better(joltage - 1, known_combos,input) + check_path_better(joltage - 2, known_combos, input) + check_path_better(joltage - 3, known_combos, input)
    


print(part2())


# returns list of list of valid joltage paths
def check_path(joltage, input, joltage_lists, current_joltage_list):
    returnable_joltage_lists = joltage_lists[:]
    if joltage == 0:
        # do something
        returnable_joltage_lists.append(current_joltage_list)
        return returnable_joltage_lists[:]
    if joltage - 1 in input:
        # something
        returnable_joltage_lists += check_path(joltage - 1, input, joltage_lists[:], (current_joltage_list + [joltage - 1])[:])
    if joltage - 2 in input:
        #something else
        returnable_joltage_lists += check_path(joltage - 2, input, joltage_lists[:], (current_joltage_list + [joltage - 2])[:])
    if joltage - 3 in input:
        # yet something else
        returnable_joltage_lists += check_path(joltage - 3, input, joltage_lists[:], (current_joltage_list + [joltage - 3])[:])
    return returnable_joltage_lists[:]