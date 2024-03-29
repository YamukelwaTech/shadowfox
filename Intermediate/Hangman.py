import random

# Predefined list of anime-related words
predefined_list = [
    "naruto",
    "dragonball",
    "onepiece",
    "bleach",
    "attackontitan",
    "deathnote",
    "pokemon",
    "myheroacademia",
]


def random_word():
    return random.choice(predefined_list)
