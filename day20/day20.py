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
    with open("input_day20.txt", "r") as reader:
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

#print(part1())


def part2():
    input_raw = []
    with open("input_day20.txt", "r") as reader:
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

    answer_dict = {'2053': {'north': '1021', 'south': '3617', 'east': '3911', 'west': '2843'}, '1543': {'north': '1663', 'south': '3581', 'east': '3529', 'west': '1949'}, '2441': {'north': '1301', 'south': '3769', 'east': '1249', 'west': '1571'}, '3733': {'north': '', 'south': '1553', 'east': '1609', 'west': '2767'}, '2237': {'north': '1117', 'south': '3299', 'east': '3877', 'west': '2113'}, '2203': {'north': '1013', 'south': '2677', 'east': '3821', 'west': '1151'}, '1783': {'north': '1949', 'south': '3037', 'east': '1627', 'west': '1607'}, '1487': {'north': '3797', 'south': '1609', 'east': '3881', 'west': ''}, '3209': {'north': '1021', 'south': '1499', 'east': '1451', 'west': '1171'}, '2557': {'north': '1979', 'south': '1637', 'east': '3323', 'west': '1871'}, '1009': {'north': '3673', 'south': '1297', 'east': '2909', 'west': ''}, '1361': {'north': '1451', 'south': '1531', 'east': '1429', 'west': '1471'}, '2767': {'north': '2741', 'south': '', 'east': '3733', 'west': '2713'}, '1109': {'north': '3203', 'south': '2083', 'east': '3347', 'west': '3821'}, '1493': {'north': '3881', 'south': '1553', 'east': '1609', 'west': '1499'}, '2971': {'north': '3769', 'south': '1583', 'east': '1193', 'west': '1249'}, '2909': {'north': '2221', 'south': '1123', 'east': '1009', 'west': '2647'}, '2551': {'north': '1307', 'south': '1297', 'east': '2341', 'west': ''}, '2917': {'north': '1319', 'south': '3727', 'east': '3467', 'west': '1789'}, '1553': {'north': '3733', 'south': '1129', 'east': '2741', 'west': '1493'}, '2297': {'north': '2389', 'south': '3529', 'east': '3541', 'west': '1663'}, '1789': {'north': '3319', 'south': '2293', 'east': '2917', 'west': ''}, '3079': {'north': '1303', 'south': '2099', 'east': '3299', 'west': ''}, '3037': {'north': '2897', 'south': '3259', 'east': '1783', 'west': '2357'}, '2677': {'north': '2203', 'south': '3529', 'east': '1987', 'west': '3581'}, '1129': {'north': '1553', 'south': '1451', 'east': '1499', 'west': '1471'}, '2647': {'north': '2357', 'south': '3851', 'east': '2897', 'west': '2909'}, '2531': {'north': '1429', 'south': '1489', 'east': '1229', 'west': '1531'}, '1663': {'north': '1063', 'south': '1543', 'east': '2297', 'west': '1777'}, '1193': {'north': '1087', 'south': '1987', 'east': '2971', 'west': '1787'}, '2477': {'north': '3541', 'south': '1117', 'east': '2389', 'west': '3877'}, '2083': {'north': '1109', 'south': '', 'east': '3407', 'west': '2927'}, '2897': {'north': '3037', 'south': '1213', 'east': '2647', 'west': '1607'}, '3797': {'north': '1487', 'south': '3643', 'east': '2377', 'west': ''}, '2087': {'north': '3917', 'south': '1847', 'east': '1613', 'west': ''}, '2447': {'north': '3617', 'south': '1213', 'east': '1607', 'west': '2843'}, '1511': {'north': '1103', 'south': '3917', 'east': '1613', 'west': ''}, '1249': {'north': '2971', 'south': '3877', 'east': '3541', 'west': '2441'}, '2741': {'north': '1553', 'south': '1259', 'east': '1471', 'west': '2767'}, '3607': {'north': '2389', 'south': '1061', 'east': '1117', 'west': '3911'}, '3877': {'north': '1301', 'south': '2477', 'east': '1249', 'west': '2237'}, '1277': {'north': '1847', 'south': '2269', 'east': '1613', 'west': '1123'}, '3491': {'north': '', 'south': '1087', 'east': '2749', 'west': '1091'}, '2011': {'north': '', 'south': '1787', 'east': '3677', 'west': '3329'}, '1087': {'north': '3491', 'south': '1193', 'east': '3769', 'west': '2459'}, '3307': {'north': '3643', 'south': '3011', 'east': '1913', 'west': ''}, '1949': {'north': '3203', 'south': '1777', 'east': '1783', 'west': '1543'}, '1061': {'north': '3607', 'south': '1237', 'east': '1289', 'west': '2969'}, '1429': {'north': '1361', 'south': '1721', 'east': '3547', 'west': '2531'}, '2221': {'north': '2341', 'south': '2909', 'east': '3851', 'west': '1297'}, '1117': {'north': '2477', 'south': '1289', 'east': '3607', 'west': '2237'}, '1571': {'north': '2749', 'south': '2099', 'east': '', 'west': '2441'}, '2969': {'north': '1061', 'south': '1021', 'east': '1171', 'west': '3911'}, '2713': {'north': '2767', 'south': '3041', 'east': '1259', 'west': ''}, '3121': {'north': '2539', 'south': '1289', 'east': '1637', 'west': '1237'}, '3673': {'north': '1847', 'south': '1009', 'east': '', 'west': '1123'}, '2683': {'north': '2539', 'south': '1823', 'east': '2377', 'west': '1237'}, '2617': {'north': '1637', 'south': '1913', 'east': '1871', 'west': '2539'}, '2341': {'north': '1229', 'south': '2551', 'east': '1489', 'west': '2221'}, '1609': {'north': '3733', 'south': '1487', 'east': '1493', 'west': ''}, '3299': {'north': '1301', 'south': '3323', 'east': '2237', 'west': '3079'}, '1259': {'north': '2713', 'south': '3467', 'east': '2741', 'west': '1319'}, '2803': {'north': '1283', 'south': '3373', 'east': '1709', 'west': ''}, '1063': {'north': '2389', 'south': '3617', 'east': '3911', 'west': '1663'}, '2113': {'north': '1637', 'south': '2237', 'east': '1289', 'west': '3323'}, '1531': {'north': '2531', 'south': '3467', 'east': '1361', 'west': '3727'}, '1289': {'north': '2113', 'south': '1061', 'east': '1117', 'west': '3121'}, '3529': {'north': '2677', 'south': '2297', 'east': '1543', 'west': '1583'}, '2389': {'north': '2297', 'south': '3607', 'east': '2477', 'west': '1063'}, '3727': {'north': '1531', 'south': '2293', 'east': '1489', 'west': '2917'}, '1013': {'north': '3329', 'south': '3407', 'east': '2203', 'west': ''}, '3373': {'north': '', 'south': '2803', 'east': '', 'west': '3011'}, '3041': {'north': '2273', 'south': '2713', 'east': '1319', 'west': ''}, '1627': {'north': '3203', 'south': '3259', 'east': '3347', 'west': '1783'}, '1297': {'north': '2551', 'south': '1009', 'east': '', 'west': '2221'}, '1787': {'north': '1151', 'south': '2459', 'east': '2011', 'west': '1193'}, '3109': {'north': '2927', 'south': '1103', 'east': '', 'west': '2287'}, '3541': {'north': '1583', 'south': '2477', 'east': '2297', 'west': '1249'}, '3347': {'north': '1109', 'south': '2287', 'east': '1627', 'west': '2927'}, '1721': {'north': '1429', 'south': '1213', 'east': '2843', 'west': '1229'}, '1847': {'north': '2087', 'south': '3673', 'east': '', 'west': '1277'}, '3329': {'north': '1151', 'south': '', 'east': '2011', 'west': '1013'}, '3881': {'north': '2377', 'south': '1493', 'east': '1823', 'west': '1487'}, '1709': {'north': '2803', 'south': '1913', 'east': '3011', 'west': '1871'}, '1171': {'north': '1823', 'south': '2969', 'east': '3209', 'west': '1237'}, '1499': {'north': '1493', 'south': '3209', 'east': '1823', 'west': '1129'}, '1283': {'north': '', 'south': '1871', 'east': '1979', 'west': '2803'}, '1637': {'north': '2557', 'south': '3121', 'east': '2617', 'west': '2113'}, '3911': {'north': '3607', 'south': '2053', 'east': '2969', 'west': '1063'}, '3259': {'north': '1627', 'south': '2269', 'east': '2287', 'west': '3037'}, '2099': {'north': '3079', 'south': '1571', 'east': '', 'west': '1301'}, '1237': {'north': '1171', 'south': '3121', 'east': '1061', 'west': '2683'}, '1987': {'north': '1193', 'south': '2677', 'east': '1583', 'west': '1151'}, '2539': {'north': '2683', 'south': '2617', 'east': '3121', 'west': '2711'}, '2269': {'north': '2357', 'south': '1321', 'east': '1277', 'west': '3259'}, '1583': {'north': '3541', 'south': '1987', 'east': '3529', 'west': '2971'}, '2749': {'north': '3491', 'south': '1571', 'east': '3769', 'west': ''}, '1613': {'north': '2087', 'south': '1321', 'east': '1511', 'west': '1277'}, '1823': {'north': '3881', 'south': '1171', 'east': '1499', 'west': '2683'}, '3821': {'north': '3407', 'south': '3581', 'east': '2203', 'west': '1109'}, '1451': {'north': '1361', 'south': '3209', 'east': '3547', 'west': '1129'}, '1913': {'north': '3307', 'south': '2617', 'east': '1709', 'west': '2711'}, '1307': {'north': '2551', 'south': '2293', 'east': '1489', 'west': ''}, '1777': {'north': '1949', 'south': '3617', 'east': '1607', 'west': '1663'}, '3011': {'north': '3307', 'south': '3373', 'east': '1709', 'west': ''}, '2459': {'north': '3677', 'south': '1087', 'east': '1787', 'west': '1091'}, '1123': {'north': '2357', 'south': '3673', 'east': '1277', 'west': '2909'}, '3917': {'north': '1511', 'south': '', 'east': '', 'west': '2087'}, '2287': {'north': '3259', 'south': '3109', 'east': '1321', 'west': '3347'}, '1471': {'north': '1129', 'south': '3467', 'east': '2741', 'west': '1361'}, '2357': {'north': '3037', 'south': '1123', 'east': '2647', 'west': '2269'}, '1319': {'north': '3319', 'south': '1259', 'east': '2917', 'west': '3041'}, '3467': {'north': '1259', 'south': '1531', 'east': '2917', 'west': '1471'}, '3407': {'north': '', 'south': '3821', 'east': '1013', 'west': '2083'}, '2801': {'north': '', 'south': '3677', 'east': '1091', 'west': ''}, '1021': {'north': '2053', 'south': '3209', 'east': '2969', 'west': '3547'}, '3677': {'north': '', 'south': '2459', 'east': '2011', 'west': '2801'}, '1321': {'north': '1103', 'south': '2269', 'east': '2287', 'west': '1613'}, '1607': {'north': '1777', 'south': '2897', 'east': '1783', 'west': '2447'}, '1979': {'north': '1303', 'south': '1283', 'east': '', 'west': '2557'}, '2927': {'north': '', 'south': '3347', 'east': '2083', 'west': '3109'}, '3203': {'north': '1109', 'south': '1949', 'east': '3581', 'west': '1627'}, '3323': {'north': '1303', 'south': '2113', 'east': '3299', 'west': '2557'}, '1489': {'north': '3727', 'south': '2341', 'east': '2531', 'west': '1307'}, '2273': {'north': '3041', 'south': '', 'east': '', 'west': '3319'}, '2293': {'north': '3727', 'south': '', 'east': '1307', 'west': '1789'}, '1301': {'north': '2099', 'south': '3877', 'east': '2441', 'west': '3299'}, '1229': {'north': '3851', 'south': '2531', 'east': '2341', 'west': '1721'}, '3769': {'north': '2441', 'south': '1087', 'east': '2971', 'west': '2749'}, '3319': {'north': '2273', 'south': '1789', 'east': '1319', 'west': ''}, '3547': {'north': '2843', 'south': '1451', 'east': '1021', 'west': '1429'}, '3643': {'north': '2711', 'south': '', 'east': '3307', 'west': '3797'}, '1103': {'north': '', 'south': '1321', 'east': '3109', 'west': '1511'}, '2711': {'north': '1913', 'south': '2377', 'east': '2539', 'west': '3643'}, '1871': {'north': '1709', 'south': '2557', 'east': '2617', 'west': '1283'}, '3851': {'north': '2221', 'south': '1213', 'east': '2647', 'west': '1229'}, '1151': {'north': '3329', 'south': '1987', 'east': '1787', 'west': '2203'}, '2377': {'north': '2711', 'south': '3881', 'east': '2683', 'west': '3797'}, '3581': {'north': '3821', 'south': '1543', 'east': '2677', 'west': '3203'}, '1303': {'north': '1979', 'south': '3079', 'east': '', 'west': '3323'}, '2843': {'north': '2053', 'south': '1721', 'east': '3547', 'west': '2447'}, '3617': {'north': '2053', 'south': '1777', 'east': '2447', 'west': '1063'}, '1091': {'north': '2801', 'south': '3491', 'east': '', 'west': '2459'}, '1213': {'north': '3851', 'south': '2447', 'east': '2897', 'west': '1721'}}
    corners = [3373, 3917, 2801, 2273]
    for item in corners:
        print(answer_dict[str(item)])
    dim = int(math.sqrt(len(tiles)))
    arr = [[0 for i in range(dim*8)] for j in range(dim*8)]
    name_arr = [["" for i in range(dim)] for j in range(dim)]
    image_arr = [[[] for i in range(dim)] for j in range(dim)]
    
    arr = place_square(tiles["2801"].image, (0, 0), arr)
    name_arr[0][0] = "2801"
    image_arr[0][0] = tiles["2801"].image


    for i in range(dim):
        for j in range(dim):
            if i == 0 and j == 0:
                continue
            neighbor_name = ""
            neighbor_image = []
            match_edge = ""
            if j - 1 < 0:
                neighbor_name = name_arr[i-1][j]
                neighbor_image = image_arr[i-1][j]
                match_edge = "south"
            else:
                neighbor_name = name_arr[i][j-1]
                neighbor_image = image_arr[i][j-1]
                match_edge = "east"
            for direction, tile_name in answer_dict[neighbor_name].items():
                if tile_name != '':
                    tile = tiles[tile_name]
                    for rotation in ["0", "90", "180", "270"]:
                        for flip in ["vertical", "horizontal", "none"]:
                            tile_transformed = transform(tile, rotation, flip)
                            if edge_match(match_edge, Tile(neighbor_name,neighbor_image), tile_transformed):
                                arr = place_square(tile_transformed.image, (i*8,j*8), arr)
                                name_arr[i][j] = tile_transformed.name

                                image_arr[i][j] = tile_transformed.image
    # scan for monster
    found_orientation = False
    for rotation in ["0", "90", "180", "270"]:
        for flip in ["vertical", "horizontal", "none"]:
            if not found_orientation:
                arr = flipper(rotate(arr, rotation), flip)
                for i in range(len(arr)):
                    for j in range(len(arr[i])):
                        is_monster = check_for_moster(arr, (i,j))
                        if is_monster:
                            found_orientation = True
                            arr = replace_monster(arr, (i,j))
            
    
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