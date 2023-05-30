"""
- Implement a program that expects exactly two command-line arguments:
    in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
    in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
- The program should then overlay shirt.png (which has a transparent background)
on the input after resizing and cropping the input to be the same size, saving the result as its output.

- Open the input with Image.open, per `pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open`,
resize and crop the input with ImageOps.fit,
per `pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit`,
using default values for method, bleed, and centering,
overlay the shirt with Image.paste, per `pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste`,
and save the result with Image.save, per `pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save`.

- The program should instead exit via sys.exit:
    - if the user does not specify exactly two command-line arguments,
    - if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
    - if the input’s name does not have the same extension as the output’s name, or
    - if the specified input does not exist.
- Assume that the input will be a photo of someone posing in just the right way,
like these demos, so that, when they’re resized and cropped, the shirt appears to fit perfectly.
"""

import sys
import os
from os import path
from PIL import Image, ImageOps

# Checking length of command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Checking for nonexistent files
elif not path.exists(sys.argv[1]):
    sys.exit("File does not exist")

else:
    # splitting the first argument given on the command-line --> given by the user
    first_arg = os.path.splitext(sys.argv[1])

    # Checking if the input’s and output’s names do not end in .jpg, .jpeg, or .png
    if first_arg[1] != ".jpeg" and first_arg[1] != ".jpg" and first_arg[1] != ".png":
        sys.exit("Invalid output")
    # Checking length of command-line argument
    elif len(sys.argv) == 3:
        # Splitting the second argument given by the user on the command-line
        second_arg = os.path.splitext(sys.argv[2])

        # Checking if the extensions of the two arguments are similar
        if first_arg[1] != second_arg[1]:
            sys.exit("Input and output have different extensions")

        else:
            # Opening an image file
            shirt = Image.open("shirt.png")
            muppet_pic = Image.open(sys.argv[1])

            # Cropping
            muppet_cropped = ImageOps.fit(
                muppet_pic,
                shirt.size,
                Image.Resampling.BICUBIC,
                bleed=0.0,
                centering=(0.5, 0.5),
            )

            # Pasting
            muppet_cropped.paste(shirt, box=None, mask=shirt)

            # Saving
            muppet_cropped.save(sys.argv[2])
