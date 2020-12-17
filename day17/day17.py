import copy
import typing
def part1():
    input_raw = []
    with open("input_day17.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    
    loc_dict = {}
    for y in range(len(input_cleaned)):
        for x in range(len(input_cleaned[y])):
            coord_tuple = (x, y, 0)
            loc_dict[coord_tuple] = input_cleaned[y][x]

    state = loc_dict.copy()
    num_cycles = 6
    i = 0
    while i < num_cycles:
        last_state = state.copy()
        state = expand_state(state)
        state = compute_next_state(state)
        i+=1
    active = count_active(state)
    return active

def expand_state(state: dict) -> dict:
    max_x, max_y, max_z, min_x, min_y, min_z = 0, 0, 0, 0, 0, 0
    for point in state.keys():
        if point[0] > max_x:
            max_x = point[0]
        if point[0] < min_x:
            min_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
        if point[1] < min_y:
            min_y = point[1]
        if point[2] > max_z:
            max_z = point[2]
        if point[2] < min_z:
            min_z = point[2]
    new_state = state.copy()
    for x in range(min_x-1,max_x+2):
        for y in range(min_y-1,max_y+2):
            for z in range(min_z-1,max_z+2):
                tuple_to_check = (x,y,z)
                if not tuple_to_check in state:
                    new_state[tuple_to_check] = "."
    return new_state

def compute_next_state(state: dict) -> dict:
    new_state = state.copy()
    for point, value in state.items():
        new_state[point] = get_update(point, value, state)
    return new_state

def get_update(point: tuple, value: str, state: dict) -> str:
    active_count = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                tuple_to_check = (point[0] + x, point[1] + y, point[2] + z)
                if tuple_to_check in state and tuple_to_check != point:
                    if state[tuple_to_check] == "#":
                        active_count += 1

    if value == "#":
        if (active_count == 2 or active_count == 3):
            return "#"
        else:
            return "."
    
    if value == ".":
        if active_count == 3:
            return "#"
        else:
            return "."

def count_active(state: dict) -> int:
    count = 0
    for value in state.values():
        if value == "#":
            count+=1
    return count



print(part1())




def part2():
    input_raw = []
    with open("input_day17.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    
    loc_dict = {}
    for y in range(len(input_cleaned)):
        for x in range(len(input_cleaned[y])):
            coord_tuple = (x, y, 0, 0)
            loc_dict[coord_tuple] = input_cleaned[y][x]

    state = loc_dict.copy()
    num_cycles = 6
    i = 0
    while i < num_cycles:
        last_state = state.copy()
        state = expand_state_2(state)
        state = compute_next_state_2(state)
        i+=1
    active = count_active_2(state)
    return active

def expand_state_2(state: dict) -> dict:
    max_x, max_y, max_z, max_w, min_x, min_y, min_z, min_w = 0, 0, 0, 0, 0, 0, 0, 0
    for point in state.keys():
        if point[0] > max_x:
            max_x = point[0]
        if point[0] < min_x:
            min_x = point[0]
        if point[1] > max_y:
            max_y = point[1]
        if point[1] < min_y:
            min_y = point[1]
        if point[2] > max_z:
            max_z = point[2]
        if point[2] < min_z:
            min_z = point[2]
        if point[3] > max_w:
            max_w = point[3]
        if point[3] < min_w:
            min_w = point[3]
    new_state = state.copy()
    for x in range(min_x-1,max_x+2):
        for y in range(min_y-1,max_y+2):
            for z in range(min_z-1,max_z+2):
                for w in range(min_w-1,max_w+2):
                    tuple_to_check = (x,y,z,w)
                    if not tuple_to_check in state:
                        new_state[tuple_to_check] = "."
    return new_state

def compute_next_state_2(state: dict) -> dict:
    new_state = state.copy()
    for point, value in state.items():
        new_state[point] = get_update_2(point, value, state)
    return new_state

def get_update_2(point: tuple, value: str, state: dict) -> str:
    active_count = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            for z in [-1, 0, 1]:
                for w in [-1, 0, 1]:
                    tuple_to_check = (point[0] + x, point[1] + y, point[2] + z, point[3] + w)
                    if tuple_to_check in state and tuple_to_check != point:
                        if state[tuple_to_check] == "#":
                            active_count += 1

    if value == "#":
        if (active_count == 2 or active_count == 3):
            return "#"
        else:
            return "."
    
    if value == ".":
        if active_count == 3:
            return "#"
        else:
            return "."

def count_active_2(state: dict) -> int:
    count = 0
    for value in state.values():
        if value == "#":
            count+=1
    return count



print(part2())



