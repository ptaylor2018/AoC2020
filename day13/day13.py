def part1():
    input_raw = []
    with open("input_day13.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    print(input_cleaned)

    min_wait_time = int(input_cleaned[0])
    bus_times = input_cleaned[1].split(",")
    good_bus_times = []
    for entry in bus_times:
        if entry != 'x':
            good_bus_times.append(int(entry))
    best_diff = 1000000000000000000000
    best_diff_line = 0
    for time in good_bus_times:
        nearest_time = (int(min_wait_time/time) + 1) * time
        diff = nearest_time - min_wait_time
        if diff < best_diff:
            best_diff = diff
            best_diff_line = time
    return best_diff*best_diff_line

print(part1())
import time

def part2():
    input_raw = []
    with open("input_day13.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    print(input_cleaned)
    bus_times = input_cleaned[1].split(",")
    good_bus_times = []
    for entry in bus_times:
        if entry != 'x':
            good_bus_times.append(int(entry))
    
    gap_dict= {}
    current_key = 0
    for i in range(len(bus_times)):
        time = bus_times[i]
        if time != 'x':
            gap_dict[int(time)] = i



    t = 0
    segment = 1


    incomplete = True

    while incomplete:
        interval = 1
        for time in good_bus_times[:segment - 1]:
            interval *= time
        not_matched = True
        while not_matched:
            if matches_condition(t, good_bus_times[:segment], gap_dict):
                segment+=1
                not_matched = False
            else:
                t+=interval
        if segment == len(good_bus_times) + 1:
            return t


def matches_condition(t, segment, gap_dict):
    for entry in segment:
        if (t + gap_dict[entry])%entry != 0:
            return False
    return True

tic = time.perf_counter()
print(part2())
toc = time.perf_counter()
print(f"Ran in {toc - tic:0.4f} seconds")
