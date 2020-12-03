def part1():
    input_raw = []
    with open('input_day2.txt', 'r') as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    #print(input_cleaned)
    valid_count = 0
    for line in input_cleaned:
        first_split = line.split("-")
        range_bottom = int(first_split[0])
        second_split = first_split[1].split(" ")
        range_top = int(second_split[0])
        letter = second_split[1][0]
        password = second_split[2]
        count = 0
        for char in password:
            if char == letter:
                count+=1
        if count <= range_top and count >= range_bottom:
            valid_count+=1
    return valid_count
#part1()

def part2():
    input_raw = []
    with open('input_day2.txt', 'r') as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    #print(input_cleaned)
    valid_count = 0
    for line in input_cleaned:
        first_split = line.split("-")
        range_bottom = int(first_split[0])
        second_split = first_split[1].split(" ")
        range_top = int(second_split[0])
        letter = second_split[1][0]
        password = second_split[2]

        if (password[range_bottom - 1] == letter) != (password[range_top - 1] == letter):
            valid_count+=1
    return valid_count

part2()