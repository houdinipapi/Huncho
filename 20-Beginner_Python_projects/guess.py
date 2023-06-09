#!/usr/bin/python3

"""
- Guess a number
"""
import random
import sys

num_list = [1, 2, 3, 4, 5]
try:
    user_num = int(input("Enter a Number: "))
    comp_num = random.choice(num_list)
except ValueError:
    sys.exit("Not a Number")
