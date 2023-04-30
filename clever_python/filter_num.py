"""
Checking how the filter() functions

"""

num_list = [1, 3, 2, 4, 5]


def is_even(numbers) -> list:

    return numbers % 2 == 0


print(list(filter(is_even, num_list)))

# This function can be summarized using lambda:

print(list(filter(lambda numbers: numbers % 2 == 0, num_list)))
