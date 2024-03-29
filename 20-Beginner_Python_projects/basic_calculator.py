"""
basic_calculator - does simple calculations.
Addition, subtraction, division, and multiplication until the user quits.
"""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    # User Input
    user_choice = input("Pick a choice: ")

    if user_choice == "a" or user_choice == "A":
        first_num = int(input("First number: "))
        second_num = int(input("Second number: "))
        print(f"Answer: {add(first_num, second_num)} \n")

    elif user_choice == "b" or user_choice == "B":
        first_num = int(input("First number: "))
        second_num = int(input("Second number: "))
        print(f"Answer: {sub(first_num, second_num)} \n")

    elif user_choice == "c" or user_choice == "C":
        first_num = int(input("First number: "))
        second_num = int(input("Second number: "))
        print(f"Answer: {mul(first_num, second_num)} \n")

    elif user_choice == "d" or user_choice == "D":
        first_num = int(input("First number: "))
        second_num = int(input("Second number: "))
        print(f"Answer: {div(first_num, second_num)} \n")

    elif user_choice == "e" or user_choice == "E":
        print("PROGRAM ENDED!")
        quit()

    else:
        print("INVALID CHOICE!!\n")
