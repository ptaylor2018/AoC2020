def part1():
    input_raw = []
    with open("small_input_day11.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    print(input_cleaned)

    state = input_cleaned[:]
    last_state = []
    while state != last_state:
        last_state = state[:]
        for row in range(len(last_state)):
            for seat in range(len(last_state[row])):
                state[row][seat] = update_seat([row, seat],last_state)
    return state

def update_seat(loc, map):
    num_empty = count_empty_around(loc, map)
    if map[loc[0]][loc[1]] == "L" and num_empty == 8:
        return "#"
    elif map[loc[0]][loc[1]] == "#" and num_empty <= 4:
        return "L"
    else:
        return map[loc[0]][loc[1]]

def count_empty_around(loc, map):
    count = 0
    if loc[0] - 1 is not < 0:
        
print(part1())