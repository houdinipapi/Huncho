#!/usr/bin/python3


def total_food(tip_percentage, food_amount):
    food_amount = input("Enter food amount: ")
    tip_percentage = input("Enter tip percentage: ")

    tip_amount = tip_percentage / 100

    total = food_amount + tip_amount
    return total


print(total_food("tip_percentage", "food_amount"))
