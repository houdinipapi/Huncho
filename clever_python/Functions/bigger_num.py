#!/usr/bin/python3


def bigger_num(num1, num2):
    """
    Given two numbers, return the bigger one.
    >>> bigger_num(3, 4)
    4
    """
    num1 = input("Insert num1: ")
    num2 = input("Insert num2: ")

    if num1 > num2:
        print(num1)
    else:
        print(num2)

    return bigger_num

bigger_num("num1", "num2")
