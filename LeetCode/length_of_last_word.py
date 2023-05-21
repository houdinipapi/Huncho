"""
Given a string `s` consisting of words and spaces, return the length of the last word in the string.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""


def length_of_last_word(s: str) -> int:
    words = s.split()  # --> splitting the string (list conversion)

    if len(words) == 0:
        return 0  # --> If the list is empty,the function returns 0

    else:
        return len(words[-1])  # --> Otherwise, it accesses the last word in the words list using the index [-1]
        # and returns its length using the len() function.


# Test Case
# s = "   fly me   to   the moon  "
# print(length_of_last_word(s))
