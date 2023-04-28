#!/usr/bin/python3

from random import choice


def random_number():
    num_range = choice(range(1, 11))

    return num_range

print(random_number())
