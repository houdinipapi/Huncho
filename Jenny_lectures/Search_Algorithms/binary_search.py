#!/usr/bin/python3

"""
Binary Search Algorithm
"""


def binary_search(user_input, target):
    user_list = sorted(user_input.split())

    print(f"Sorted list: {user_list}")

    low = 0
    high = len(user_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if user_list[mid] == target:
            return mid
        elif user_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main_func():
    user_input = input("Enter items separated by a space:\n")
    target = input("Target: ")

    result = binary_search(user_input, target)

    if result != -1:
        return f"Target found at index: {result}"
    else:
        return "Target not found"


print(main_func())
