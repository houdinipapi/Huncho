def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    k = 1
    for i in range(1, len(nums)):

