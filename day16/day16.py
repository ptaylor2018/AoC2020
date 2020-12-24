def part1():
    input_raw = []
    with open("input_day16.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    #print(input_cleaned)

    breaks = [i for i,x in enumerate(input_cleaned) if x=='']
    
    rules = input_cleaned[:breaks[0]]
    rules_dict = {}

    for entry in rules:
        first = entry.split(":")
        name = first[0]
        second = first[1].split(" ")
        range_1 = second[1].split("-")
        range_2 = second[3].split("-")
        range_1_bottom = int(range_1[0])
        range_1_top = int(range_1[1])
        range_2_bottom = int(range_2[0])
        range_2_top = int(range_2[1])
        rules_dict[name] = (range_1_bottom, range_1_top, range_2_bottom, range_2_top)

    your_ticket = list(map(int,input_cleaned[breaks[0]+2:breaks[1]][0].split(",")))
    nearby_tickets = list(map(lambda x: list(map(int,x.split(","))),input_cleaned[breaks[1]+2:]))
    
    score = 0
    for ticket in nearby_tickets:
        validity = check_validity(ticket, rules_dict)
        if validity != "Valid":
            score += validity
        

    return score

def check_validity(ticket, rules_dict):
    score = 0
    for number in ticket:
        is_valid = False
        for name, rule in rules_dict.items():
            if number >= rule[0] and number <= rule[1] or number >= rule[2] and number <= rule[3]:
               is_valid = True
        if not is_valid:
            score += number
    if score == 0:
        return "Valid"
    else:
        return score
            
print(part1())

def part2():
    input_raw = []
    with open("input_day16.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    #print(input_cleaned)

    breaks = [i for i,x in enumerate(input_cleaned) if x=='']
    
    rules = input_cleaned[:breaks[0]]
    rules_dict = {}

    for entry in rules:
        first = entry.split(":")
        name = first[0]
        second = first[1].split(" ")
        range_1 = second[1].split("-")
        range_2 = second[3].split("-")
        range_1_bottom = int(range_1[0])
        range_1_top = int(range_1[1])
        range_2_bottom = int(range_2[0])
        range_2_top = int(range_2[1])
        rules_dict[name] = (range_1_bottom, range_1_top, range_2_bottom, range_2_top)

    your_ticket = list(map(int,input_cleaned[breaks[0]+2:breaks[1]][0].split(",")))
    nearby_tickets = list(map(lambda x: list(map(int,x.split(","))),input_cleaned[breaks[1]+2:]))
    
    score = 0
    good_tickets = []
    for ticket in nearby_tickets:
        validity = check_validity(ticket, rules_dict)
        if validity != "Valid":
            score += validity
        else:
            good_tickets.append(ticket)
    possibility_dict = {}
    for i in range(len(good_tickets[0])):

        name_list = []
        for name, rule in rules_dict.items():
            name_list.append(name)
        possibility_dict[i] = name_list

    for ticket in good_tickets:
        for place, number in enumerate(ticket):
            possibilities = possibility_dict[place]
            new_possibilities = []
            for possibility in possibilities:
                rule = rules_dict[possibility]
                if number >= rule[0] and number <= rule[1] or number >= rule[2] and number <= rule[3]:
                    new_possibilities.append(possibility)
            possibility_dict[place] = new_possibilities
            if len(new_possibilities) == 1:
                possibility_dict = strike_others(new_possibilities[0], possibility_dict)
    print(possibility_dict)

    product = 1
    for key, value in possibility_dict.items():
        if value[0].startswith("departure"):
            product = product * your_ticket[key]

    return product

def strike_others(entry, poss_dict):
    for key, value in poss_dict.items():
        if entry in value and len(value) > 1:
            value.remove(entry)
            poss_dict[key] = value
            if len(value) == 1:
                poss_dict = strike_others(value[0], poss_dict)
    return poss_dict

print(part2())