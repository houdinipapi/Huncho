#!/usr/bin/python3

random_string = input("Enter a random word: ")
try:
    new_random_string = int(random_string)
except:
    new_random_string = -1
