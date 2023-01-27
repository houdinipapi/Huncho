#!/usr/bin/python3

food_amount = float(input("Enter your food amount: "))
tip_percentage = float(input("Enter your tip %: ")) / 100
tip_amount = food_amount * tip_percentage

total = food_amount + tip_amount
print("\n\n\n")
print(f"Food Amount: ${food_amount}")
