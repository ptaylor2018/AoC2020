import typing

def part1():
    # for testing only
    # card_public_key = 5764801
    # door_public_key = 17807724

    #card_public_key = 5099500
    #door_public_key = 7648211

    
    door_loop_size = get_loop_size(door_public_key)
    card_loop_size = get_loop_size(card_public_key)

    encryption_key = do_transform(card_loop_size, door_public_key)
    return encryption_key


def do_transform(loop_size, subject_number):
    value = 1
    for i in range(loop_size):
        value = value * subject_number
        value = value % 20201227  
    return value

def get_loop_size(public_key):
    loop_size = 1
    value = 1
    not_done = True
    while not_done:
        value = value * 7
        value = value % 20201227
        if value == public_key:
            not_done = False
        else:
            loop_size += 1
    return loop_size

print(part1())