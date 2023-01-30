#!/usr/bin/python3


def total_food(tip_percentage: int, food_amount: int) -> int:
    food_amount = input("Enter food amount: ")
    tip_percentage = input("Enter tip percentage: ")

    tip_amount = int(food_amount) * (int(tip_percentage) / 100)

    total = int(food_amount) + tip_amount
    return total


print(total_food("tip_percentage", "food_amount"))
