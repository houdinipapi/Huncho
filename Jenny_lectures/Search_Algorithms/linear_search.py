#!/usr/bin/python3

"""
Linear Search Algorithm
"""


def linear_search(user_input, target):
    user_list = user_input.split()

    for index, item in enumerate(user_list):
        if item == target:
            return f"Target was found at index: {index}"
        break


def main_func():
    user_input = input("Enter items separated by space:\n")
    target = input("Target: ")
    result = linear_search(user_input, target)
    print(result)


main_func()
