def part1():
    input_cleaned = [0,8,15,2,12,1,4]
    history = input_cleaned[:]
    i = len(input_cleaned)
    while i < 2020:
        number_in_question = history[-1]
        occurences = [i for i,x in enumerate(history[:-1]) if x==number_in_question]
        if len(occurences) == 0:
            history.append(0)
        else:
            history.append(i - occurences[-1] - 1)
        i+=1

    return history[-1]

print(part1())

def part2():
    input_cleaned = [0,8,15,2,12,1,4]
    last_place_dict = {}
    for i, entry in enumerate(input_cleaned[:-1]):
        last_place_dict[entry] = i
    #print(last_place_dict)
    i = len(input_cleaned)
    next_num = input_cleaned[-1]
    while i < 30000000:
        #print(i)
        number_in_question = next_num
        if not number_in_question in last_place_dict:
            next_num = 0
        else:
            diff = i - last_place_dict[number_in_question] - 1
            next_num = diff
        last_place_dict[number_in_question] = i - 1
        i+=1
        #print(last_place_dict, next_num)

    return next_num

print(part2())