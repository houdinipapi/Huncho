"""
Implement a program that prompts the user for the answer to the Great Question of Life,
the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
Otherwise, output No.
"""

answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
if answer == 42:
    print("Yes")
elif answer == "forty-two" or "Forty-Two":
    print("Yes")
elif answer == "forty two" or "Forty Two":
    print("Yes")
else:
    print("No")
