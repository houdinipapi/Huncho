#!/usr/bin/python3

"""
- Guess a number
"""
import random
import sys

num_list = [1, 2, 3, 4, 5]
comp_num = random.choice(num_list)

while True:
    if len(sys.argv) < 2:
        sys.exit("Few Commands")
    else:
        try:
            user_num = int(sys.argv[1])

            if user_num == comp_num:
                sys.exit("CORRECT MATCH")
            else:
                continue
        except ValueError:
            sys.exit("Not a Number")
