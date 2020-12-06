def part1():
    input_raw = []
    with open("input_day6.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip().replace("\n", " "))

    for group in input_cleaned:
        entries = doc.split()
