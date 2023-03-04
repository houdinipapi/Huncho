#!/usr/bin/python3

import random

names = input("Enter names spaciously: ")
names_split = names.split(" ")
print(names_split)

names_length = len(names_split)
rand_name = random.randint(0, names_length - 1)
print(names_split[rand_name])
