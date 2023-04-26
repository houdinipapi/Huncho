"""
Create a function that given a list of numbers,
it can return their sum
>>> sum_list([3, 4, 2])
9
"""


def sum_list(numbers: list[int]) -> int:
    count = 0
    for num in numbers:
        count += num
    return count


print(sum_list([3, 4, 5]))
