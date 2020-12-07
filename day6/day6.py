def alphabet_position(text):
    nums = [str(ord(x) - 96) for x in text.lower() if x >= 'a' and x <= 'z']
    return " ".join(nums)

def part1():
    input_raw = []
    with open('input_day6.txt', 'r') as reader:
        # Read and print the entire file line by line
        current_entry = ""
        for line in reader:
            if line == "\n":
                input_raw.append(current_entry)
                current_entry = ""
            else:
                current_entry +=line
        input_raw.append(current_entry)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip().replace("\n",""))

    group_sums = []
    for group in input_cleaned:
        checked = [0 for i in range(26)]
        nums = alphabet_position(group)
        for num in nums.split():
            if checked[int(num) - 1] == 0:
                checked[int(num) - 1] = 1
        group_sum = sum(checked) 
        group_sums.append(group_sum)
    return sum(group_sums)

print(part1())

def part2():
    input_raw = []
    with open('input_day6.txt', 'r') as reader:
        # Read and print the entire file line by line
        current_entry = ""
        for line in reader:
            if line == "\n":
                input_raw.append(current_entry)
                current_entry = ""
            else:
                current_entry +=" " +line
        input_raw.append(current_entry)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip().replace("\n","").split())

    group_sums = []
    for group in input_cleaned:
        checked = [0 for i in range(26)]
        nums = alphabet_position(group[0])
        for num in nums.split():
            if checked[int(num) - 1] == 0:
                checked[int(num) - 1] = 1
        for person in group[1:]:
            for i in range(26):
                if checked[i] == 1:
                    if not chr(ord('`')+i+1) in person:
                        checked[i] = 0
        group_sum = sum(checked) 
        group_sums.append(group_sum)
    return sum(group_sums)

print(part2())