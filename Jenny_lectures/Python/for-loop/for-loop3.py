#!/usr/bin/python3

'''
for loop - traversing through a sequence
'''

nums = [3, 5, 7, 9, -4]
square_list = []

for i in nums:
    square = i ** 2
    print(square)
    square_list.append(square)
print(f"The new list is: {square_list}")
