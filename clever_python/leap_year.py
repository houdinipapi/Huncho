#!/usr/bin/python3

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        print("Leap Year")
        if year % 400 == 0:
            print("Not a Leap Year")
        else:
            print("Leap Year")
    else:
        print("Not a Leap Year")
else:
    print("Not a leap Year")
