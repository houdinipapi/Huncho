"""
Filtering even numbers in a list
>>> list(filter(lambda num: num % 2 == 0, [4, 5, 6, 8]))
[4, 6, 8]
"""

numbers = [2, 3, 4, 5, 7]
print(list(filter(lambda num: num % 2 == 0, numbers)))
