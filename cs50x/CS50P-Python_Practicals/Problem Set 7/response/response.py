"""
- Implement a program that prompts the user for
an email address via input.
- Prints Valid or Invalid, respectively, if the input is
a syntatically valid email address.
- No use of 're'.
- Do not validate whether the email address's
domain name actuall exists.
"""

from validators import email


def main():
    user_email = input("What's your email address? ")

    if email(user_email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()