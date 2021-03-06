def part1():
    input_raw = []
    with open("input_day14.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())

    memory = {}
    mask = ""
    line_stripped = []
    for line in input_cleaned:
        line_split = line.split("=")
        line_stripped.append([line_split[0].strip(), line_split[1].strip()])
        #print(line_stripped)
    for entry in line_stripped:
        #print(entry)
        if entry[0] == 'mask':
            mask = entry[1]
        elif entry[0][:3] == "mem":
            address = entry[0][4:-1]
            to_mask = int(entry[1])
            memory[address] = do_mask(mask, to_mask)
    memory_sum = 0
    #print(memory)
    for key, value in memory.items():
        memory_sum += value

    return memory_sum

def do_mask(mask, to_mask):
    to_one_mask = ""
    to_zero_mask = ""
    for char in mask:
        if char == "X":
            to_one_mask += "0"
            to_zero_mask += "1"
        elif char == "1":
            to_one_mask += "1"
            to_zero_mask += "1"
        elif char == "0":
            to_one_mask += "0"
            to_zero_mask += "0"
    int_mask_one = int(to_one_mask, 2)
    int_mask_zero = int(to_zero_mask, 2)
    return int((int_mask_one | to_mask) & int_mask_zero)

print(part1())


def part2():
    input_raw = []
    with open("input_day14.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())

    memory = {}
    mask = ""
    line_stripped = []
    for line in input_cleaned:
        line_split = line.split("=")
        line_stripped.append([line_split[0].strip(), line_split[1].strip()])
        #print(line_stripped)
    for entry in line_stripped:
        #print(entry)
        if entry[0] == 'mask':
            mask = entry[1]
        elif entry[0][:3] == "mem":
            address = entry[0][4:-1]
            to_mask = int(address)
            value = int(entry[1])
            addr_list = do_mask_2(mask, to_mask)
            for addr in addr_list:
                memory[addr] = value
    memory_sum = 0
    #print(memory)
    for key, value in memory.items():
        memory_sum += value

    return memory_sum

def do_mask_2(mask, to_mask):
    to_mask_bin = bin(to_mask)
    just_num = to_mask_bin[2:]
    padding = (36 - len(just_num)) * "0"
    just_num_padded = padding + just_num

    result_string = ""
    num_x = 0

    for rule, char in zip(mask, just_num_padded):
        if rule == "1":
            result_string += "1"
        elif rule == "X":
            result_string += "X"
            num_x+=1
        elif rule == "0":
            result_string += char
    #print(result_string)
    addr_strings = []
    for i in range(2**num_x):
        fitted_string = ""
        bin_i = bin(i)[2:]
        padding = (num_x - len(bin_i)) * "0"
        bin_i = padding + bin_i
        #print(bin_i)
        for char in result_string:
            if char == "X":
                #print(bin_i[0])
                fitted_string += bin_i[0]
                bin_i = bin_i[1:]
            else:
                fitted_string += char
        addr_strings.append(fitted_string)

    return addr_strings

print(part2())