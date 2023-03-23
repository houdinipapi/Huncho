#!/usr/bin/python3
"""
A rock, paper, and scissor game
"""

import random

user_choice = int(input("Pick a number: (0 - Rock, 1 - Paper, 2 - Scissor) "))
comp_choice = random.randint(0, 2)
print(comp_choice)
print(user_choice)
