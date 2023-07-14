#!/usr/bin/python3

"""
- Linear Search
"""

list1 = [23, 45, 83, 21, 13, 27]
target = 83

for index, item in enumerate(list1):
    # print(f"Index: {index}, Item: {item}")
    if item == target:
        print(index)
