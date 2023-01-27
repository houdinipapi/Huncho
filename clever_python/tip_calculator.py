#!/usr/bin/python3

food_amount = float(input("Enter your food amount: "))
tip_percentage = float(input("Enter your tip %: ")) / 100
tip_amount = food_amount * tip_percentage

#print("$" + str(tip_amount))

total = food_amount + tip_amount
print("$" + str(total))
print(type(total))
