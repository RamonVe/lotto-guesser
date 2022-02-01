import random


def random_items():
    item_list = open('items/item_list.txt', 'r').readlines()

    random_one = random.choice(item_list)
    random_two = random.choice(item_list)
    random_three = random.choice(item_list)
    random_four = random.choice(item_list)
    random_five = random.choice(item_list)

    random_item_list = [random_one, random_two, random_three, random_four, random_five]

    return random_item_list
