"""
- implement a program that:
    Expects zero or two command-line arguments:
    Zero if the user would like to output text in a random font.
    Two if the user would like to output text in a specific font,
    in which case the first of the two should be -f or --font,
    and the second of the two should be the name of the font.
- Prompts the user for a str of text.
- Outputs that text in the desired font.
- If the user provides two command-line arguments and the first is not -f or --font
  or the second is not the name of a font, the program should exit via sys.exit with an error message.
"""

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    text = input("Input: ")
    font = random.choice(figlet.getFonts())
    figlet.setFont(font=font)
    print(f"Output: {figlet.renderText(text)}")
elif len(sys.argv) > 1:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in figlet.getFonts():
            text = input("Input: ")
            font = sys.argv[2]
            figlet.setFont(font=font)
            print(f"Output: {figlet.renderText(text)}")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
