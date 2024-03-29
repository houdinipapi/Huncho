"""
- In Massachusetts, it’s possible to request a vanity license plate for your car,
with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end.
For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
- Implement a program that prompts the user for a vanity plate and then
output Valid if meets all the requirements or Invalid if it does not.
- Assume that any letters in the user’s input will be uppercase.
"""


def is_valid(s):
    if 2 > len(s) > 6:
        return False
    elif not s[:2].isalpha():
        return False

    new_num = False
    for char in s[2:]:
        if not char.isalnum():
            return False
        elif char.isnumeric():
            if not new_num and char == "0":
                return False
            new_num = True
        else:
            if new_num:
                return False
    return True


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    print(main())
