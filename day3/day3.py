def part1():
    input_raw = []
    with open('input_day3.txt', 'r') as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    
    slope_width = len(input_cleaned[0])

    horiz_pos = 0

    trees = 0
    for row in input_cleaned:
        if row[horiz_pos] == "#":
            trees+=1
        horiz_pos += 3
        if horiz_pos >= slope_width:
            horiz_pos -= slope_width
    return trees
print(part1())

def part2():
    input_raw = []
    with open('input_day3.txt', 'r') as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    
    slope_width = len(input_cleaned[0])
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    treesProd = 1
    for slope in slopes:
        horiz_pos = 0
        vert_pos = 0
        trees = 0
        while vert_pos < len(input_cleaned):
            if input_cleaned[vert_pos][horiz_pos] == "#":
                trees+=1
            horiz_pos += slope[0]
            vert_pos += slope[1]
            if horiz_pos >= slope_width:
                horiz_pos -= slope_width
        treesProd = treesProd * trees
    return treesProd
print(part2())