"""
a function that returns the maximum number in a list
>>> find_max([1, 2, 3])
3
"""


def find_max(numbers: list[int]) -> int:
    current_max = numbers[0]

    for i in numbers:
        if i > current_max:
            current_max = i

    return current_max


print(find_max([59, 60, 61]))
