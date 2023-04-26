"""
Find even numbers in a list
>>> even_list([3, 5, 6, 2, 8])
[6, 2, 8]
"""


def even_list(numbers: list) -> list:
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num)

    return result


print(even_list([1, 2, 3, 4, 5, 6]))
