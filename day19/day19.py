def part1():
    input_raw = []
    with open("small_input_day19.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())

    split_point = input_cleaned.index('')

    rules = input_cleaned[:split_point]
    messages = input_cleaned[split_point+1:]
    #print(rules, messages)
    rules_dict = {}
    for rule in rules:
        first = rule.split(":")
        rule_name = first[0]
        first_rules = []
        second_rules = []
        if "|" in first[1]:
            rule_contents = first[1][1:].split("|")
            first_rules = rule_contents[0].strip(" ").split(" ")
            second_rules = rule_contents[1].strip(" ").split(" ") 
        else:
            first_rules = first[1].strip(" ").split(" ")
        #print(first_rules, second_rules)
        rules_dict[rule_name] = (first_rules, second_rules)

    count = 0
    for message in messages:
        if (fulfills_rules(message, rules_dict)):
            count +=1

    return count

def fulfills_rules(message, rules_dict):
    
    def get_rule_length(rule):
        print(rule)
        if rules_dict[rule][0] == '"a"' or rules_dict[rule][0] == '"b"':
            return 1
        else:
            rule_parts = rules_dict[rule]
            sum = 0
            for part in rule_parts:
                sum += get_rule_length(part)
            return sum

    def check_rule(message, rule):
        if rules_dict[rule] == '"a"' :
            if message == "a":
                return True
            else:
                return False
        elif rules_dict[rule] == '"b"':
            if message == "b":
                return True
            else:
                return False
        else:
            start_place = 0
            truth = True
            print(rules_dict[rule])
            for part in rules_dict[rule][0]:
                length = get_rule_length(part)
                truth = truth and check_rule(message[start_place:start_place+length], part)
                start_place = start_place+length
            start_place = 0
            truth2 = True
            for part in rules_dict[rule][1]:
                length = get_rule_length(part)
                truth2 = truth2 and check_rule(message[start_place:start_place+length], part)
                start_place = start_place+length
            return truth or truth2


    

    check_rule(message, '0')


print(part1())