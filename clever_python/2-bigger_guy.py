"""
Write a function bigger_guy that takes in two numbers
and returns the bigger one
MAKE SURE to use RETURN and not PRINT in the function
"""


def bigger_guy(a: int, b: int) -> int:

    if a > b:
        return a
    elif b > a:
        return b
    else:
        return 0


print(bigger_guy(3, 6))
