#!/usr/bin/python3

food_amount = float(input("Enter your food amount: "))
tip_percentage = float(input("Enter your tip %: ")) / 100
tip_amount = food_amount * tip_percentage

total = food_amount + tip_amount
print("\n\n")
print("-------------------------------")
print(f"Food Amount: ${food_amount}")
print(f"Tip Percentage: ${tip_percentage}")
print(f"Tip Amount: ${tip_amount}")
print(f"Total Amount: ${total}")
