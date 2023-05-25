"""
Implement a program that prompts the user for the name of a variable in camel case and,
outputs the corresponding name in snake case.
Assume that the user’s input will indeed be in camel case.
"""


def case_conversion(camelCase):
    snake_case = ""
    for char in camelCase:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip('_')


def main():
    camel_case = input("camelCase: ")
    return f"snake_case: {case_conversion(camelCase=camel_case)}"


if __name__ == "__main__":
    print(main())
