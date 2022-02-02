import random as r


def random_pair():
    item_list = open('item_list', 'r').readlines()

    random_item_list = r.sample(item_list, len(item_list))

    pure_random_items = []
    for item in random_item_list:
        pure_random_items.append(item.strip())

    n = 77
    number_list = [i + 1 for i in range(n)]

    random_number_list = r.sample(number_list, len(number_list))

    random_pairing = {}
    for key in random_number_list:
        for value in pure_random_items:
            random_pairing[key] = value
            pure_random_items.remove(value)
            break

    return random_pairing


print(random_pair())
