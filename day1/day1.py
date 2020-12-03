def part1():
    input = []
    with open('input.txt', 'r') as reader:
        # Read and print the entire file line by line
        for line in reader:
            input.append(line)
    input_cleaned = []
    for item in input:
        input_cleaned.append(int(item.rstrip()))
    #print(input_cleaned)

    for item in input_cleaned:
        diff = 2020 - item
        for sub_item in input_cleaned:
            if(sub_item == diff):
                print(sub_item, item)
                return sub_item*item
print(part1())

def part2():
    input = []
    with open('input.txt', 'r') as reader:
        # Read and print the entire file line by line
        for line in reader:
            input.append(line)
    input_cleaned = []
    for item in input:
        input_cleaned.append(int(item.rstrip()))
    #print(input_cleaned)

    for num1 in input_cleaned:
        diff1 = 2020 - num1
        for num2 in input_cleaned:
            diff2 = diff1 - num2
            for num3 in input_cleaned:
                if(num3 == diff2):
                    print(num1, num2, num3)
                    return num1*num2*num3
print(part2())
