#!/usr/bin/python3

"""
- Guess a number
"""
import random
import sys

num_list = [1, 2, 3, 4, 5]
comp_num = random.choice(num_list)

while True:
    user_num = int(input("Guess a number: "))
    try:
        if user_num == comp_num:
            print("CORRECT MATCH")
            sys.exit(0)
        else:
            print("Try Again")
            continue
                
    except ValueError:
        print("Invalid Input")
        sys.exit(1)
