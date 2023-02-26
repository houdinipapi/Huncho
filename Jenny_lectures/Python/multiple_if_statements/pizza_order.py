#!/usr/bin/python3

print("Order your pizza")
print("S. Small Pizza\nM. Medium Pizza\nL. Large Pizza")
pizza_size = input("Pick a letter: ")
bill = 0

if pizza_size == 'S' or pizza_size == 's':
    bill += 10
    print("Small Pizza price is $10")

elif pizza_size == 'M' or pizza_size == 'm':
    bill += 15
    print("Medium Pizza price is $15")

elif pizza_size == 'L' or pizza_size == 'l':
    bill += 20
    print("Large Pizza price is $20")


add_pepperoni = input("Do you want pepperoni? (Y/N) ")
if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if pizza_size == 'S' or pizza_size == 's':
        bill += 3

    else:
        bill += 5

extra_cheese = input("Would you like extra cheese? (Y/N) ")
if extra_cheese == 'Y' or extra_cheese == 'y':
    bill += 2

print(f"Your total bill is ${bill}")
