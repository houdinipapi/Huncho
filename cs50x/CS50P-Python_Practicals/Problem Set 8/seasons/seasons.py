"""
- Implement a program that prompts the user for their date of birth in
    YYYY-MM-DD format and then sings prints how old they are in minutes,
    rounded to the nearest integer, using English words instead of numerals,
    just like the song from Rent, without any and between words.
- Since a user might not know the time at which they were born, assume,
    for simplicity, that the user was born at midnight (i.e., 00:00:00)
    on that date.
- And assume that the current time is also midnight.
    In other words, even if the user runs the program at noon,
    assume that it’s actually midnight, on the same date.
- Use datetime.date.today to get today’s date.
"""

from datetime import date, datetime
import inflect
import sys


def get_birthday():
    # Getting user's birthdate
    birthday = input("Date of Birth: ")

    # Validating the format: --> Expacts YYYY-MM-DD
    try:
        birthday = date.fromisoformat(birthday)
        return birthday

    # Exiting the program if given an invalid date
    except ValueError:
        sys.exit("Invalid Date")


def calculate_age_in_mins(birthday):
    # Calculating age in minutes

    # Getting current date
    current_date = date.today()

    # Calculating days
    age_in_days = (current_date - birthday).days

    # Converting days into minutes
    age_in_mins = age_in_days * (24 * 60)
    return age_in_mins


def print_age_in_mins(age_words):
    # Using inflect lib to convert age(numerical) into words
    # Also omitting 'and' as required
    p = inflect.engine()
    age_words = p.number_to_words(age_words, andword="")
    return f"{age_words.capitalize()} minutes"


# Main function
def main():
    birthday = get_birthday()
    age_in_mins = calculate_age_in_mins(birthday)
    print(print_age_in_mins(age_in_mins))


if __name__ == "__main__":
    main()
