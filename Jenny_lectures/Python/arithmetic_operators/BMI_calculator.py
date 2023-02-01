#!/usr/bin/python3
weight = input("Enter your weight in kilograms: ")
height = input("Enter your height in meteres: ")
weight = float(weight)
height = float(height)
BMI_calc = weight / (height ** 2)
print(BMI_calc)
