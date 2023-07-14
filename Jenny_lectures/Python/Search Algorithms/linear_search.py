#!/usr/bin/python3

"""
- Linear Search
"""

# list1 = [23, 45, 83, 21, 13, 27]
user_input = input("Enter items separated by space: ")
list1 = user_input.split()
# print(list1)
target = input("Target: ")

for index, item in enumerate(list1):
    # print(f"Index: {index}, Item: {item}")
    if item == target:
        print(f"Target found at index: {index}")
        break
print("Target not found")
