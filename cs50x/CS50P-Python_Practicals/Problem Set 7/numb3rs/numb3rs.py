#!/usr/bin/python3
"""
- Implement a function called validate that expects an IPv4 address as input
as a str and then returns True or False, respectively,
if that input is a valid IPv4 address or not.
"""

import re
# import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    # Checking for matches
    matches = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    # Checking if the matches are present in the input
    if re.match(matches, ip) is not None:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
