#!/usr/bin/python3


def bigger_num(num1: int, num2: int) -> int:
    """
    Given two numbers, return the bigger one.
    >>> bigger_num(3, 4)
    4
    """
    num1 = input("Insert num1: ")
    num2 = input("Insert num2: ")

    if num1 > num2:
        return num1
    else:
        return num2


print(bigger_num("num1", "num2"))
