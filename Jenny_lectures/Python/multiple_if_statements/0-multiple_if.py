#!/usr/bin/python3

age = int(input("What is your age? "))
height = int(input("What is your height? "))
bill = 0

if height >= 3:
    print("You can ride.")
    if age <= 12:
        bill = 15
        print("Your bill is $15.")
    elif age <= 18:
        bill = 20
        print("Your bill is $20.")
    else:
        bill = 25
        print("Your bill is $25.")

    want_photo = input("Would you like to take a photo(Y/N)? ")
    if want_photo == 'y' or want_photo == 'Y':
        bill += 5
    print(f"Your total bill is {bill}")
else:
    print("You cannot ride!!")
print("Thank you!!")
