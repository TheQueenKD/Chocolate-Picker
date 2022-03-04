import random


TYPES = [
    'a',
    'b',
    'c',
]


def pick_chocolate(quantity):
    pick = random.sample(TYPES, quantity)
    return pick


if __name__ == '__main__':
    quantity = int(input('How many do you want to eat?:\t'))
    print(f'You should eat: {pick_chocolate(quantity)}')
