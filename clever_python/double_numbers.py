"""
doubles each number in a list
"""


def double_num(numbers: list) -> list:
    result = []

    for num in numbers:
        result.append(num * 2)

    return result


print(double_num([1, 2, 3]))
