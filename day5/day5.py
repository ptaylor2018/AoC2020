def part1():
    input_raw = []
    with open("input_day5.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())

    seat_ids = []
    for bpass in input_cleaned:
        row_component = bpass[:6]
        row_range = [num for num in range(128)]
        for letter in row_component:
            if letter == "F":
                row_range = row_range[: len(row_range) // 2]
            elif letter == "B":
                row_range = row_range[len(row_range) // 2 :]
        row_num = row_range[0]

        col_component = bpass[-3:]
        col_range = [num for num in range(8)]
        for letter in col_component:
            if letter == "L":
                col_range = col_range[: len(col_range) // 2]
            elif letter == "R":
                col_range = col_range[len(col_range) // 2 :]
        col_num = col_range[0]

        seat_ids.append(row_num * 8 + col_num)

    return max(seat_ids)


print(part1())


def part2():
    input_raw = []
    with open("input_day5.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())

    seat_id_grid = [[0 for i in range(8)] for j in range(128)]
    for bpass in input_cleaned:
        row_component = bpass[:7]
        row_range = [num for num in range(128)]
        for letter in row_component:
            if letter == "F":
                row_range = row_range[: len(row_range) // 2]
            elif letter == "B":
                row_range = row_range[len(row_range) // 2 :]
        row_num = row_range[0]

        col_component = bpass[-3:]
        col_range = [num for num in range(8)]
        for letter in col_component:
            if letter == "L":
                col_range = col_range[: len(col_range) // 2]
            elif letter == "R":
                col_range = col_range[len(col_range) // 2 :]
        col_num = col_range[0]

        seat_id_grid[row_num][col_num] = 1

    for row in range(128):
        for col in range(8):

            if (
                seat_id_grid[row][col] == 0
                and seat_id_grid[row][col - 1] == 1
                and seat_id_grid[row][col + 1] == 1
            ):
                if col - 1 > -1 and col + 1 < 9:
                    return row * 8 + col


print(part2())
