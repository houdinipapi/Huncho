#!/usr/bin/python3

"""
    adding all even numbers within a specific range
"""
nums = range(1, 101)
total = 0
for i in nums:
    if i % 2 == 0:
        total += i
print(total)
