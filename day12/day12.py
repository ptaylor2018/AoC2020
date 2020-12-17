import typing
import copy
def part1():
    input_raw = []
    with open("input_day12.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    # x, y
    pos = [0, 0]
    heading = 0

    for step in input_cleaned:
        instr = step[0]
        value = int(step[1:])
        if instr == "N":
            pos[1] += value
        if instr == "E":
            pos[0] += value
        if instr == "S":
            pos[1] -= value
        if instr == "W":
            pos[0] -= value
        if instr == "L":
            heading += value
            if heading >= 360:
                heading -= 360
        if instr == "R":
            heading -= value
            if heading < 0:
                heading += 360
        if instr == "F":
            if heading == 0:
                pos[0] += value
            if heading == 90:
                pos[1] += value
            if heading == 180:
                pos[0] -= value
            if heading == 270:
                pos[1] -= value

    manhattan_distance = abs(pos[0])+abs(pos[1])
    return manhattan_distance

print(part1())

def part2():
    input_raw = []
    with open("input_day12.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    # x, y
    ship_pos = [0, 0]
    beacon_pos = [10, 1]

    for step in input_cleaned:
        instr = step[0]
        value = int(step[1:])
        if instr == "N":
            beacon_pos[1] += value
        if instr == "E":
            beacon_pos[0] += value
        if instr == "S":
            beacon_pos[1] -= value
        if instr == "W":
            beacon_pos[0] -= value
        if value == 180:
            beacon_pos = [beacon_pos[0] * -1, beacon_pos[1] * -1]
        if value == 90 and instr == "L" or value == 270 and instr == "R":
            beacon_pos = [-1 * beacon_pos[1], beacon_pos[0]]
        if value == 90 and instr == "R" or value == 270 and instr == "L":
            beacon_pos = [beacon_pos[1], -1 * beacon_pos[0]]
        if instr == "F":
            ship_pos = [ship_pos[0]+beacon_pos[0]*value, ship_pos[1]+beacon_pos[1]*value]

    manhattan_distance = abs(ship_pos[0])+abs(ship_pos[1])
    return manhattan_distance

print(part2())