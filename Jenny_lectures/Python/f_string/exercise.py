#!/usr/bin/python3

current_year = int(input("Enter the current year: "))
next_election_year = int(input("Enter the next election year: "))
rem_months = (next_election_year - current_year) * 12
rem_weeks = (next_election_year - current_year) * 52

print(f"{rem_months} months and {rem_weeks} weeks remaining till the next general election.")
