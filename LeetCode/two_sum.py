""" Give a list of integers [nums] and an integer 'target',
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.
>>> two_sum([2, 7, 11, 15], 9)
[0, 1]
"""


def two_sum(nums, target):
    num_table = dict()  # --> Create an empty dictionary to store each number and its index.

    # -- enumerate() -- #
    # When given a list, the enumerate() function returns an enumerate object
    # which contains pairs of elements of the list and their indices(counters)
    # e.g.,
    # my_list = ['Papi', 'Chulo', 'Houdini']
    # for index, item in enumerate(my_list):
    #     print(index, item)
    #
    # >>> 0 Papi
    # >>> 1 Chulo
    # >>> 2 Houdini

    for index, num in enumerate(nums):  # --> Iterate over each number in the list.
        complement = target - num

        if complement in num_table:  # --> Check if the complement of the current number is in the dictionary.
            return [num_table[complement], index]  # --> Return the indices of the two numbers.

        num_table[num] = index  # --> Add the current number to the dictionary.

    return []  # --> If no solution is found, return an empty list.


print(two_sum([11, 7, 2, 15], 9))
