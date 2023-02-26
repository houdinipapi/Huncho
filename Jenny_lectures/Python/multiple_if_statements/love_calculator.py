#!/usr/bin/python3

print("LOVE CALCULATOR")

first_name = input("What's your name? ")
second_name = input("What's your partner's name? ")

both_names = first_name + second_name
lower_case_names = both_names.lower()

t = lower_case_names.count('t')
r = lower_case_names.count('r')
u = lower_case_names.count('u')
e = lower_case_names.count('e')
true = t + r + u + e

l = lower_case_names.count('l')
o = lower_case_names.count('o')
v = lower_case_names.count('v')
e = lower_case_names.count('e')
love = l + o + v + e

love_percent = str(true) + str(love)

print(f"Your love percentage is {love_percent}")

if int(love_percent) < 10 or int(love_percent) > 90:
    print("Perfect Match")

elif int(love_percent) > 40 and int(love_percent) < 60:
    print("Better Match")

else:
    print("Good Match")
