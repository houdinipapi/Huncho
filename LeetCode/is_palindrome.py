"""
Checks if a number is a palindrome.
**A palindrome is a word, phrase, number, or other sequence of characters that reads the same backward and forward.**
>>> is_palindrome(343)
True
>>> is_palindrome(-343)
False
"""


def is_palindrome(x: int) -> bool:  # --> Takes an integer 'x' as input and expects to return a boolean.
    return str(x) == str(x)[::-1]  # --> x is converted into a string 'str()' to enable string slicing notation.


print(is_palindrome(787))

# --- NOTE -- #
# - The function takes an integer and converts it into a string using the 'str()' function.
# - It then applies string slicing notation to reverse the string,
# - and then compares it to the original string using the '==' operator.
# - If both values match, the function returns 'True', meaning that the input is a palindrome.
# - Otherwise it returns 'False'.
