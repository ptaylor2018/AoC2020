def part1():
    input_raw = []
    with open('input_day4.txt', 'r') as reader:
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
        input_cleaned.append(item.rstrip().replace("\n"," "))

    needed_parts = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_count = 0
    for doc in input_cleaned:
        entries = doc.split()
        parts = []
        for entry in entries:
            entry_split = entry.split(":")
            parts.append(entry_split[0])
        check = all(item in parts for item in needed_parts)
        if check is True:
            valid_count+=1
    return valid_count
print(part1())

import string
def part2():
    input_raw = []
    with open('input_day4.txt', 'r') as reader:
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
        input_cleaned.append(item.rstrip().replace("\n"," "))

    valid_count = 0
    for doc in input_cleaned:
        entries = doc.split()
        parts = list(map(lambda s: s.split(":"),entries))
        valid_part_count = 0
        for part in parts:
            if part[0] == "byr":
                if(int(part[1]) >= 1920 and int(part[1]) <= 2002):
                    valid_part_count+=1
            elif part[0] == "iyr":
                if(int(part[1]) >= 2010 and int(part[1]) <= 2020):
                    valid_part_count+=1
            elif part[0] == "eyr":
                if(int(part[1]) >= 2020 and int(part[1]) <= 2030):
                    valid_part_count+=1
            elif part[0] == "hgt":
                if part[1][-2:] == "cm":
                    if int(part[1][:-2]) >= 150 and int(part[1][:-2]) <= 193:
                        valid_part_count+=1
                elif part[1][-2:] == "in":
                    if int(part[1][:-2]) >= 59 and int(part[1][:-2]) <= 76:
                        valid_part_count+=1
            elif part[0] == "hcl":
                if len(part[1]) == 7:
                    if part[1][0] == "#":
                        if all(c in string.hexdigits for c in part[1][1:]):
                            valid_part_count+=1
            elif part[0] == "ecl":
                if part[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    valid_part_count+=1
            elif part[0] == "pid":
                if len(part[1]) == 9:
                    if all(c in '0123456789' for c in part[1]):
                            valid_part_count+=1
        if valid_part_count == 7:
            valid_count+=1
    return valid_count
print(part2())



