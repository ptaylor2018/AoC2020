import typing
import math
def part1():
    input_raw = []
    with open("small_input_day22.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())

    current_player = ""
    player_1_cards = []
    player_2_cards = []
    for line in input_cleaned:
        if len(line)> 0 and line[0] == "P":
            current_player = line
        else:
            if current_player == "Player 1:":
                player_1_cards.append(int(line))
            else: 
                player_2_cards.append(int(line))

    while len(player_1_cards) > 0 and len(player_2_cards) > 0:
        p1_card = player_1_cards.pop(0)
        p2_card = player_2_cards.pop(0)
        if p1_card > p2_card:
            player_1_cards.append(p1_card)
            player_1_cards.append(p2_card)
        else:
            player_2_cards.append(p2_card)
            player_2_cards.append(p1_card)
    

    if len(player_1_cards) == 0:
        sum = 0
        player_2_cards.reverse()
        for i, card in enumerate(player_2_cards):
            sum += (i+1)*card
        return sum
    else:
        sum = 0
        player_1_cards.reverse()
        for i, card in enumerate(player_1_cards):
            sum += (i+1)*card
        return sum
print(part1())