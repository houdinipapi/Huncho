"""
Implement a program that prompts the user for the answer to the Great Question of Life,
the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
Otherwise, output No.
"""


def deep_program():
    answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
    answer = answer.strip().lower().replace(" ", "")  # Removing leading/trailing spaces, converting to lowercase, and removing spaces inside

    if answer == "42" or answer == "fortytwo" or "forty-two":
        print("Yes")
    else:
        print("No")


deep_program()
