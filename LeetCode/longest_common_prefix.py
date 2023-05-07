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
