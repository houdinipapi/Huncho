#!/usr/bin/python3
"""
A function that uses try() and except() keywords
"""


def try_and_except():
    user_input = input("Enter a random input: ")
    try:
        new_user_input = int(user_input)
    except:
        new_user_input = -1

    if new_user_input > 0:
