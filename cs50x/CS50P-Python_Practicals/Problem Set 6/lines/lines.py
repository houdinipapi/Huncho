"""
- Implement a program that expects exactly one command-line argument,
the name (or path) of a Python file, and outputs the number of lines of code in that file,
excluding comments and blank lines.
- If the user does not specify exactly one command-line argument,
or if the specified file’s name does not end in .py,
or if the specified file does not exist, the program should instead exit via sys.exit.
- Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
(A docstring should not be considered a comment.)
Assume that any line that only contains whitespace is blank.
"""
import sys

# -- try and catch error -- #
try:
    # Handling length of command-line arguments
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Handling files that do not end with ".py"
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    else:
        # Opening the file & reading--> given as an argument on the command line
        with open(sys.argv[1], 'r') as file:
            # Reading each line in the file
            lines = file.readlines()
            # Initiating count of lines
            count = 0

            # Iterating through the lines:
            for line in lines:
                # Removing white-space
                line = line.strip()
                # Checking for comments --> starts with #
                if not line.startswith("#"):
                    # If line has content i.e., after stripping whitespace and skipping comments
                    if len(line) > 0:
                        count += 1
            # Printing the number of lines in the file(count)
            print(f"Lines: {count}")
# Handling a "file does not exist" error
except FileNotFoundError:
    sys.exit("File does not exist")
