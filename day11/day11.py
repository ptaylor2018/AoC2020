import typing
import copy
def part1():
    input_raw = []
    with open("input_day11.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    input_cleaned = list(map(split, input_cleaned))
        
    #print(input_cleaned)

    state = copy.deepcopy(input_cleaned)
    last_state = []
    while state != last_state:
        last_state = copy.deepcopy(state)
        for row in range(len(last_state)):
            for seat in range(len(last_state[row])):
                #print(update_seat([row, seat],last_state))
                state[row][seat] = update_seat([row, seat],last_state)
    full_seats = 0
    for row in state:
        for seat in row:
            if seat =="#":
                full_seats+=1
    return full_seats

def split(word): 
    return [char for char in word]  

def update_seat(loc, map):
    num_full = count_full_around(loc, map)
    if map[loc[0]][loc[1]] == "L" and num_full == 0:
        return "#"
    elif map[loc[0]][loc[1]] == "#" and num_full >= 4:
        return "L"
    else:
        return map[loc[0]][loc[1]]

def count_full_around(loc, map):
    count = 0
    if not loc[0] - 1 < 0 and not loc[1] - 1 < 0:   #
        if map[loc[0] - 1][loc[1] - 1] == "#":       #
            count+=1                                #
    if not loc[0] - 1 < 0:                          
        if map[loc[0] - 1][loc[1]] == "#":             
            count+=1
    if not loc[0] - 1 < 0 and not loc[1] + 1 >= len(map[0]):
        if map[loc[0] - 1][loc[1] + 1] == "#":
            count+=1
    if not loc[1] + 1 >= len(map[0]):
        if map[loc[0]][loc[1] + 1] == "#":
            count+=1
    if not loc[0] + 1 >= len(map) and not loc[1] + 1 >= len(map[0]):
        if map[loc[0]+ 1][loc[1] + 1] == "#":
            count+=1
    if not loc[0] + 1 >= len(map):
        if map[loc[0]+ 1][loc[1]] == "#":
            count+=1
    if not loc[0] + 1 >= len(map) and not loc[1] - 1 < 0:
        if map[loc[0]+ 1][loc[1] - 1] == "#":
            count+=1 
    if not loc[1] - 1 < 0:
        if map[loc[0]][loc[1] - 1] == "#":
            count+=1  
    return count
    
print(part1())

import copy
def part2():
    input_raw = []
    with open("input_day11.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    input_cleaned = list(map(split, input_cleaned))
        
    #print(input_cleaned)

    state = copy.deepcopy(input_cleaned)
    last_state = []
    while state != last_state:
        last_state = copy.deepcopy(state)
        for row in range(len(last_state)):
            for seat in range(len(last_state[row])):
                #print(update_seat([row, seat],last_state))
                state[row][seat] = update_seat_2([row, seat],last_state)
    full_seats = 0
    for row in state:
        for seat in row:
            if seat =="#":
                full_seats+=1
    return full_seats

def update_seat_2(loc, map):
    num_full = count_full_around_2(loc, map)
    if map[loc[0]][loc[1]] == "L" and num_full == 0:
        return "#"
    elif map[loc[0]][loc[1]] == "#" and num_full >= 5:
        return "L"
    else:
        return map[loc[0]][loc[1]]

def count_full_around_2(loc, map):
    count = 0
    dirs = [(-1,-1),(-1, 0),(-1, 1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for dir in dirs:
        count += check_dir(dir, loc, map)
    return count

def check_dir(dir: tuple, loc: list, map: list) -> int:
    seat = [loc[0] + dir[0], loc[1] + dir[1]]
    if (isValidSeat(seat, map)):
        if map[seat[0]][seat[1]] == "#":
            return 1
        elif map[seat[0]][seat[1]] == "L":
            return 0
        else:
            return check_dir(dir, seat, map)
    else: 
        return 0

def isValidSeat(seat: list, map: list) -> bool:
    if seat[0] < 0:
        return False
    if seat[0] >= len(map):
        return False
    if seat[1] < 0:
        return False
    if seat[1] >= len(map[0]):
        return False
    return True


print(part2())