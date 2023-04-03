#!/usr/bin/python3
firstName = input("What is your first name?")
middleName = input("What is your middle name?")
temp = firstName
firstName = middleName
middleName = temp
print("firstName = ", firstName)
print("middleName = ", middleName)
