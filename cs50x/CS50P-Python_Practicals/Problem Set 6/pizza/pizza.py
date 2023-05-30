"""
- Implement a program that expects exactly one command-line argument,
the name (or path) of a CSV file in Pinocchio’s format,
and outputs a table formatted as ASCII art using tabulate,
a package on PyPI at pypi.org/project/tabulate.
- Format the table using the library’s grid format.
- If the user does not specify exactly one command-line argument,
or if the specified file’s name does not end in .csv,
or if the specified file does not exist, the program should instead exit via sys.exit.
"""
import sys
import csv
from tabulate import tabulate

# -- try and catch error -- #
try:
    # Checking command-line length
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Checking for a CSV file
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    else:
        # Opening the file
        with open(sys.argv[1]) as file:
            # Reading a CSV file
            reader = csv.reader(file, delimiter=',')
            headers = next(reader)

            # Creating Tables
            tables = []
            for row in reader:
                tables.append(row)
            print(tabulate(tables, headers, tablefmt="grid"))

# Handling nonexistent file
except FileNotFoundError:
    sys.exit("File does not exist")
