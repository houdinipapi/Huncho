# def remove_duplicates(nums):
#     if len(nums) == 0:
#         return 0
#
#     k = 1
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i - 1]:
#             nums[k] = nums[i]
#             k += 1
#
#     return k
#
#
# print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))


"""
- Given an integer list [nums] sorted in ascending order,
remove the duplicates in-place such that each unique element appears only once.
- The relative order of the elements should be kept the same.
- Then return the number of unique elements in [nums].
- Consider the number of unique elements of [nums] to be k, to get accepted, you need to do the following things:
    - Change the list [nums] such that the first k elements of [nums] contain the unique elements in the order
    they were present in [nums] initially.
    - The remaining elements of [nums] are not important as well as the size of [nums].
    - Return k.

>>> remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
5
"""

def
