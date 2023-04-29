"""
Checking how the filter() functions

"""

num_list = [1, 3, 2, 4, 5]


def is_even(numbers) -> list:

    return numbers % 2 == 0


print(list(filter(is_even, num_list)))


