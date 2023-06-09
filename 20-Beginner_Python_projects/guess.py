#!/usr/bin/python3

"""
- Guess a number
"""
import random
import sys


try:
    user_num = int(input("Enter a Number: ")
except ValueError:
    sys.exit("Not a Number")
