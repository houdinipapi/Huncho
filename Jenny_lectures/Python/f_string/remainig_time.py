#!/usr/bin/python3

age = int(input("Enter your age: "))
target_age = int(input("Enter your target age: "))
rem_months = (target_age - age) * 12
rem_weeks = (target_age - age) * 52
rem_days = (target_age - age) * 365

print(f"You have {rem_months} months, {rem_weeks} weeks, and {rem_days} days remaining till you reach {target_age} years")
