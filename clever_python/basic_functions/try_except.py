#!/usr/bin/python3

random_string = input("Enter a random input: ")
try:
    new_random_string = int(random_string)
except:
    new_random_string = -1

if new_random_string > 0:
    print("INTEGER")
else:
    print("STRING")
