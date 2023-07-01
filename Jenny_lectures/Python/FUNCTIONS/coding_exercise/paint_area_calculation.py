import math


def paint_calculation(height, width, coverage):
    area = height * width
    no_of_cans = math.ceil(
        area / coverage
    )  # ceil() --> rounding off to the next number
    return f"Cans needed: {no_of_cans}"


wall_height = int(input("Height: "))
wall_width = int(input("Width: "))
wall_coverage = 7

print(paint_calculation(height=wall_height, width=wall_width, coverage=wall_coverage))
