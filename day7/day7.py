def part1():
    input_raw = []
    with open("input_day7.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())

    rule_dict = {}
    for rule in input_cleaned:
        words = rule.split()
        color = " ".join(words[:2])
        contents = " ".join(words[4:]).split(",")
        contents_list = []
        if contents[0] != "no other bags.":
            for content in contents:
                fixed = content.split()
                num = fixed[0]
                color_inner = fixed[1] + " " + fixed[2]
                contents_list.append([num, color_inner])
        rule_dict[color] = contents_list

    count = 0
    for key, value in rule_dict.items():
        count += check_contents(key, rule_dict)
    return count


def check_contents(bag, rule_dict):
    count = 0
    for bag_inner in rule_dict[bag]:
        if bag_inner[1] == "shiny gold":
            count += 1
        else:
            count += check_contents(bag_inner[1], rule_dict)
    if count >= 1:
        return 1
    else:
        return 0


print(part1())


def part2():
    input_raw = []
    with open("input_day7.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())

    rule_dict = {}
    for rule in input_cleaned:
        words = rule.split()
        color = " ".join(words[:2])
        contents = " ".join(words[4:]).split(",")
        contents_list = []
        if contents[0] != "no other bags.":
            for content in contents:
                fixed = content.split()
                num = fixed[0]
                color_inner = fixed[1] + " " + fixed[2]
                contents_list.append([num, color_inner])
        rule_dict[color] = contents_list

    return count_bags("shiny gold", rule_dict)


def count_bags(bag, rule_dict):
    count = 0
    for inner_bag in rule_dict[bag]:
        count += int(inner_bag[0]) + count_bags(inner_bag[1], rule_dict) * int(
            inner_bag[0]
        )
    return count


print(part2())