def part1():
    input_raw = []
    with open("small_input_day7.txt", "r") as reader:
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
                color = fixed[1] + " " + fixed[2]
                contents_list.append([num, color])
        rule_dict[color] = contents_list
    print(rule_dict)


print(part1())