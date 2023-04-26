"""
>>> list(map(double_num, [1, 2, 3]))
[2, 4, 6]
"""


def double_num(number):
    return number * 2


print(list(map(double_num, [9, 5, 3])))
