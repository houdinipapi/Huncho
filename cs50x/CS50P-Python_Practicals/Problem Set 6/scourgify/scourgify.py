"""
- Implement a program that:
    - Expects the user to provide two command-line arguments:
        - the name of an existing CSV file to read as input, whose columns are assumed
        to be, in order, name and house, and
        - the name of a new CSV to write as output, whose columns should be,
        in order, first, last, and house.
    - Converts that input to that output, splitting each name into a first name and last name.
    - Assume that each student will have both a first name and last name.
- If the user does not provide exactly two command-line arguments,
or if the first cannot be read, the program should exit via sys.exit with an error message.
"""

import csv
import sys

# -- try and catch error -- #
try:
    # Checking length of the command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    else:
        # Initiating an empty list
        students = list()

        # Opening a file
        with open(sys.argv[1]) as file:
            # Reading the file --> {Dictionary Reader}
            reader = csv.DictReader(file)
            # Iterating through the file contents
            for row in reader:
                # Accessing the key name and splitting it into two
                names = row["name"].split(', ')
                first_name = names[1]
                last_name = names[0]
                house = row["house"]
                # Appending the keys and values to the list
                students.append({'first': first_name, 'last': last_name, 'house': house})

                # Extracting the keys(column names) from the first dictionary in the 'students' list
                keys = students[0].keys()

                # Opening and writing a new file
                with open(sys.argv[2], 'w', newline="") as new_file:
                    writer = csv.DictWriter(new_file, keys)
                    writer.writeheader()
                    writer.writerows(students)

            # Handling nonexistent file
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
