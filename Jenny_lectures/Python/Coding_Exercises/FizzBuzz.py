#!/usr/bin/python3

"""
    if number is divisible by 3 - print Fizz
    if number is divisible by 5 - print Buzz
    if number is divisible by both 3 and 5 - print FizzBuzz
"""

user_range = int(input("Enter the range: "))
for num in range(1, (user_range + 1)):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")

    else:
        print(num)
