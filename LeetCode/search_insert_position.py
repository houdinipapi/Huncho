"""
Given a sorted list of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""


# The function takes in the sorted list and a target value
def search_insert(nums: list, target: int) -> int:
    # Initializing two pointers to the start and end of the list respectively
    left = 0
    right = len(nums) - 1

    while left <= right:
        # Computes the middle index `mid` using integer division
        mid = left + (right - left) // 2

        # Comparing the value at middle index with the target value
        if nums[mid] == target:  # --> If middle index value is equal to the target, the function returns middle index.
            return mid

        elif nums[mid] < target:  # --> If middle index value is less than the target, left pointer becomes `mid + 1`
            left = mid + 1

        else:  # --> If middle index value is greater than the target, right pointer becomes `mid - 1`
            right = mid - 1

    return left  # --> If target not found in list, return `left` pointer,
    # which represents the index where the target would be inserted.


print(search_insert([1, 3, 5, 6], 5))
