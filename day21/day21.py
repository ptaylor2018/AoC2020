import typing
import copy
def part1():
    input_raw = []
    with open("input_day21.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    # value is set of possible allergens that ingredient might be
    ingredient_dict: dict[set] = {}
    # value is set of foods that definitely contain that allergen
    allergen_dict: dict[set] = {}
    food_list = []

    for i, line in enumerate(input_cleaned):
        #split into ingredients and allergens
        halves = line.split("(")
        ingredients = halves[0][:-1].split(" ")
        allergens = halves[1][9:].replace(" ","").strip(")").split(",")
        #print(ingredients, allergens)
        food_list.append(ingredients)

        for ingredient in ingredients:
            if not ingredient in ingredient_dict:
                ingredient_dict[ingredient] = set([])
            ingredient_dict[ingredient] = ingredient_dict[ingredient] | set(allergens)
        for allergen in allergens:
            if not allergen in allergen_dict:
                allergen_dict[allergen] = set([])
            allergen_dict[allergen] = allergen_dict[allergen] | set([i])


    for ingredient, allergens in ingredient_dict.items():
        new_allergens = allergens.copy()
        for allergen in allergens:
            not_valid = False
            for food in allergen_dict[allergen]:
                if ingredient not in food_list[food]:
                    not_valid = True
                    break
        
            if not_valid == True:
                new_allergens.remove(allergen) 
        ingredient_dict[ingredient] = new_allergens

    count = 0
    for ingredient, allergens in ingredient_dict.items():
        if len(allergens) == 0:
            for food in food_list:
                if ingredient in food:
                    count+=1
    return count
print(part1())

def part2():
    input_raw = []
    with open("input_day21.txt", "r") as reader:
        # Read and print the entire file line by line
        for line in reader:
            input_raw.append(line)
    input_cleaned = []
    for item in input_raw:
        input_cleaned.append(item.rstrip())
    # value is set of possible allergens that ingredient might be
    ingredient_dict: dict[set] = {}
    # value is set of foods that definitely contain that allergen
    allergen_dict: dict[set] = {}
    food_list = []

    for i, line in enumerate(input_cleaned):
        #split into ingredients and allergens
        halves = line.split("(")
        ingredients = halves[0][:-1].split(" ")
        allergens = halves[1][9:].replace(" ","").strip(")").split(",")
        #print(ingredients, allergens)
        food_list.append(ingredients)

        for ingredient in ingredients:
            if not ingredient in ingredient_dict:
                ingredient_dict[ingredient] = set([])
            ingredient_dict[ingredient] = ingredient_dict[ingredient] | set(allergens)
        for allergen in allergens:
            if not allergen in allergen_dict:
                allergen_dict[allergen] = set([])
            allergen_dict[allergen] = allergen_dict[allergen] | set([i])


    for ingredient, allergens in ingredient_dict.items():
        new_allergens = allergens.copy()
        for allergen in allergens:
            not_valid = False
            for food in allergen_dict[allergen]:
                if ingredient not in food_list[food]:
                    not_valid = True
                    break
        
            if not_valid == True:
                new_allergens.remove(allergen) 
        ingredient_dict[ingredient] = new_allergens

    count = 0
    ingredient_dict_compact = {}
    for ingredient, allergens in ingredient_dict.items():
        if len(allergens) != 0:
            ingredient_dict_compact[ingredient] = allergens

    #print(ingredient_dict_compact)
    all_unclaimed_ingredients = []
    all_unclaimed_allergens = []
    for ingredient, allergens in ingredient_dict_compact.items():
        if ingredient not in all_unclaimed_ingredients:
            all_unclaimed_ingredients.append(ingredient)
        for allergen in allergens:
            if allergen not in all_unclaimed_allergens:
                all_unclaimed_allergens.append(allergen)
    #print(all_unclaimed_allergens)
    #print(all_unclaimed_ingredients)
    final_dict = {}
    tempi = 0
    while len(final_dict) < len(all_unclaimed_ingredients):
        #print(ingredient_dict_compact)
        for allergen, ingredient in final_dict.items():
            for key, value in ingredient_dict_compact.items():
                #print(allergen)
                if allergen in value:
                    value.remove(allergen)
                    ingredient_dict_compact[key] = value
                   # print(ingredient_dict_compact)
        for ingredient, allergens in ingredient_dict_compact.items():
            if len(allergens) == 1:
                final_dict[list(allergens)[0]] = ingredient
       # print("here")
        tempi +=1
    #print(final_dict)
    all_unclaimed_allergens.sort()
    final_list = []
    for allergen in all_unclaimed_allergens:
        final_list.append(final_dict[allergen])
    
    return ",".join(final_list)

print(part2())

