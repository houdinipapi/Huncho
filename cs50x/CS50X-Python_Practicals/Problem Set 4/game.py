"""
- Implement a program that:
    Prompts the user for a level, n.
    If the user does not input a positive integer, the program should prompt again.
    Randomly generates an integer between 1 and, inclusive, using the random module.
- Prompts the user to guess that integer.
    If the guess is not a positive integer, the program should prompt the user again.
    If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    If the guess is the same as that integer, the program should output Just right! and exit.
"""

import sys
import random

while True:
    try:
        user_level = int(input("Level: "))
        if user_level < 1:
            continue
        else:
            random_integer = random.randint(1, user_level)

        user_guess = int(input("Guess: "))
        if user_guess < 1:
            continue
        elif user_guess < random_integer:
            print("Too small!")
