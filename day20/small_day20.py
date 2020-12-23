import typing
import copy
import math

class Tile:
    def __init__(self, name, image):
        self.name = name
        self.image = image

    def show(self):
        for row in self.image:
            print(row)

def part1():
    input_raw = []
    with open("small_input_day20.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    #print(input_cleaned)
    current_image = []
    current_title = ""
    tiles = []
    for line in input_cleaned:
        if len(line) == 0:
            tiles.append(Tile(current_title, current_image))
            current_image = []
            current_title = ""
        elif line[0] == "T":
            current_title = line[5:-1]
        elif line[0] == "." or line[0] == "#":
            current_image.append(list(line))
    tiles.append(Tile(current_title, current_image))
    print(len(tiles))
    answer_dict = {}
    for i, tile in enumerate(tiles):
        tiles_copy = tiles[:]
        del tiles_copy[i]
        print(i, tile.name)
        answer_dict[tile.name] = find_neighbors(tile, tiles_copy)
    corners = []
    print(answer_dict)
    for tile, neighbors in answer_dict.items():
        count = 0
        for direction, neighbor in neighbors.items():
            if neighbor == "":
                count += 1
        if count == 2:
            corners.append(int(tile))
    print(corners)
    return math.prod(corners)
    
def find_neighbors(tile: Tile, tiles: list) -> dict:
    neighbors = {
        "north": "",
        "south":"",
        "east":"",
        "west":""
    }
    for other_tile in tiles:
        comparison = compare(tile, other_tile)
        if comparison != "Not Neighbors":
            neighbors[comparison] = other_tile.name
    return neighbors
def compare(tile: Tile, other_tile: Tile) -> str:
    for direction in ["north", "east", "south", "west"]:
        for rotation in ["0", "90", "180", "270"]:
            for flip in ["vertical", "horizontal", "none"]:
                other_tile_transformed = transform(other_tile, rotation, flip)
                if edge_match(direction, tile, other_tile_transformed):
                    #print(direction, tile.name, other_tile_transformed.name)
                    return direction
    return "Not Neighbors"
def transform(tile: Tile, rotation: str, flip: str) -> Tile:
    image = tile.image
    new_image = copy.deepcopy(image)
    new_image = rotate(new_image, rotation)
    new_image = flipper(new_image, flip)
    return Tile(tile.name, new_image)
def rotate(image: list, rotation) -> list:
    new_image = copy.deepcopy(image)
    if rotation == "0":
        return new_image
    elif rotation == "90":
        new_image = list(zip(*image))[::-1]
        newer_image = []
        for line in new_image:
            newer_image.append(list(line))
        return newer_image
    elif rotation == "180":
        return flipper(flipper(new_image, "horizontal"), "vertical")
    elif rotation == "270":
        return rotate(rotate(new_image, "180"), "90")

def flipper(image: list, flip):
    new_image = copy.deepcopy(image)
    if flip == "none":
        return new_image
    elif flip == "horizontal":
        for i, line in enumerate(image):
            for j, char in enumerate(line):
                new_image[i][j] = image[i][len(line) - 1 - j]
    elif flip == "vertical":
        for i, line in enumerate(image):
            for j, char in enumerate(line):
                if j <0:
                    print(j)
                new_image[i][j] = image[len(image) - 1 - i][j]
    return new_image

def edge_match(direction, tile, other_tile):
    if direction == "north":
        if tile.image[0] == other_tile.image[-1]:
            return True
        else:
            return False
    if direction == "south":
        if tile.image[-1] == other_tile.image[0]:
            return True
        else:
            return False   
    if direction == "east":
        if rotate(tile.image, "90")[0] == rotate(other_tile.image, "90")[-1]:
            return True
        else:
            return False 
    if direction == "west":
        if rotate(tile.image, "270")[0] == rotate(other_tile.image, "270")[-1]:
            return True
        else:
            return False 

print(part1())


def part2():
    input_raw = []
    with open("small_input_day20.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    #print(input_cleaned)
    current_image = []
    current_title = ""
    tiles = {}
    for line in input_cleaned:
        if len(line) == 0:
            tiles[current_title] = Tile(current_title, current_image)
            current_image = []
            current_title = ""
        elif line[0] == "T":
            current_title = line[5:-1]
        elif line[0] == "." or line[0] == "#":
            current_image.append(list(line))
    tiles[current_title] = Tile(current_title, current_image)

    answer_dict = {'2311': {'north': '1427', 'south': '', 'east': '3079', 'west': '1951'}, '1951': {'north': '2729', 'south': '', 'east': '2311', 'west': ''}, '1171': {'north': '2473', 'south': '', 'east': '1489', 'west': ''}, '1427': {'north': '1489', 'south': '2311', 'east': '2473', 'west': '2729'}, '1489': {'north': '', 'south': '1427', 'east': '1171', 'west': '2971'}, '2473': {'north': '', 'south': '1427', 'east': '3079', 'west': '1171'}, '2971': {'north': '', 'south': '2729', 'east': '1489', 'west': ''}, '2729': {'north': '2971', 'south': '1951', 'east': '1427', 'west': ''}, '3079': {'north': '', 'south': '2473', 'east': '', 'west': '2311'}}
    corners = [1951, 1171, 2971, 3079]
    for item in corners:
        print(answer_dict[str(item)])
    dim = int(math.sqrt(len(tiles)))
    print(dim)
    arr = [[0 for i in range(dim*8)] for j in range(dim*8)]
    name_arr = [["" for i in range(dim)] for j in range(dim)]
    image_arr = [[[] for i in range(dim)] for j in range(dim)]
    
    arr = place_square(flipper(tiles["1951"].image, "vertical"), (0, 0), arr)
    name_arr[0][0] = "1951"
    image_arr[0][0] = flipper(tiles["1951"].image, "vertical")


    for i in range(dim):
        for j in range(dim):
            if i == 0 and j == 0:
                continue
            neighbor_name = ""
            neighbor_image = []
            match_edge = ""
            #print(name_arr, i, j)
            if j - 1 < 0:
                neighbor_name = name_arr[i-1][j]
                neighbor_image = image_arr[i-1][j]
                match_edge = "south"
                print("here", neighbor_name)
            else:
                neighbor_name = name_arr[i][j-1]
                neighbor_image = image_arr[i][j-1]
                match_edge = "east"
            print(neighbor_name)
            for direction, tile_name in answer_dict[neighbor_name].items():
                if tile_name != '':
                    tile = tiles[tile_name]
                    for rotation in ["0", "90", "180", "270"]:
                        for flip in ["vertical", "horizontal", "none"]:
                            tile_transformed = transform(tile, rotation, flip)
                            if edge_match(match_edge, Tile(neighbor_name,neighbor_image), tile_transformed):
                                arr = place_square(tile_transformed.image, (i*8,j*8), arr)
                                name_arr[i][j] = tile_transformed.name
                                print(match_edge, i, j, neighbor_name, tile_transformed.name)
                                image_arr[i][j] = tile_transformed.image
    for line in arr:
        print(line)
    # scan for monster
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for rotation in ["0", "90", "180", "270"]:
                for flip in ["vertical", "horizontal", "none"]:
                    is_monster = check_for_moster(flipper(rotate(arr, rotation), flip), (i,j))
                    if is_monster:
                        arr = replace_monster(flipper(rotate(arr, rotation), flip), (i,j))
    
    count = 0
    for row in arr:
        for char in row:
            if char == "#":
                count +=1
    #for row in arr:
     #   print(row)
    return count
   
def check_for_moster(arr:list, loc: tuple) -> str:
    monster = [list("                  # "),list("#    ##    ##    ###"),list(" #  #  #  #  #  #   ")]
    count = 0
    for i, row in enumerate(monster):
        for j, char in enumerate(row):
            if char == "#":
                if loc[0]+i < len(arr) and loc[1]+j < len(arr[0]):
                    if arr[loc[0]+i][loc[1]+j] == "#":
                        count += 1
    #print(count)
    if count == 15:
        return True
    return False
def replace_monster(arr: list, loc: tuple) -> list:
    print("here!")
    monster = [list("                  # "),list("#    ##    ##    ###"),list(" #  #  #  #  #  #   ")]
    for i, row in enumerate(monster):
        for j, char in enumerate(row):
            if char == "#":
                if arr[loc[0]+i][loc[1]+j] == "#":
                    arr[loc[0]+i][loc[1]+j] = "0"
    return arr

def place_square(image: list, loc: tuple, arr: list) -> list:
    image_stripped = []
    for row in image:
        image_stripped.append(row[1:-1])
    image_stripped = image_stripped[1:-1]

    for i, row in enumerate(image_stripped):
        for j, char in enumerate(row):
            arr[loc[0]+i][loc[1]+j] = char
    return arr

print("total count:", part2())