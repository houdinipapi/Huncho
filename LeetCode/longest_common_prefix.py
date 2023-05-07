"""
Test cases:
>>> longest_common_prefix(['milk', 'mist', 'mike'])
'mi'
"""


def longest_common_prefix(strs: list[str]) -> str:
    """
    Finds the longest common prefix string amongst a list of strings.
    If there is no common prefix, returns an empty string
    :param strs: ['flower', 'floor', 'flog']
    :return: 'flo'
    """

    # Assume the first string as the prefix
    prefix = strs[0]

    # Loop through each string from the second string onwards
    for s in strs[1:]:
        # While the prefix is not in the beginning of the string, remove one character from the prefix
        while prefix and not s.startswith(prefix):
            prefix = prefix[:-1]

        # If the prefix becomes empty, there is no common prefix, thus return an empty string
        if not prefix:
            return ""

    return prefix


print(longest_common_prefix(['just', 'jug', 'jump']))

# --- SOLUTION EXPLANATION --- #

# The function takes a list of strings 'strs' as an input.
# It first checks if the given list is empty.
# If the list is empty, it returns an empty string since there can be no common prefix in an empty list.
# If the given list is not empty, the function initializes 'prefix' to be the first string in the list.
# The function then loops through each string in the list. N/B:- It starts looping from the second string onwards.
# The function removes characters from 'prefix' until it is a prefix of the current string 's'.
# If 'prefix' becomes empty, then there is no common prefix, thus an empty string is returned.

# --- END --- #
