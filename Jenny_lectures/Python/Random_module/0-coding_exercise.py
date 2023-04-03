#!/usr/bin/python3

import random

names = input("Enter names spaciously: ")
names_split = names.split(" ")
print(names_split)

random_name = random.choice(names_split)
print(random_name)
