"""
Given a string 's' containing the characters '(', ')', '{', '}', '[', and ']',
determine if the input string is valid.
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.
>>> is_valid("()[]{}")
True
>>> is_valid("(]")
False
"""


def is_valid(s: str) -> bool:
    # Create a dictionary of opening brackets as keys and closing brackets as values
    brackets_dict = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    # Create an empty list to keep tack of the opening brackets
    lst = list()

    # Loop through each character in the input string
    for char in s:
        # If the character is an opening bracket, push it onto the list
        if char in brackets_dict:
            lst.append(char)

        # If the character is a closing bracket, pop the last opening bracket from the list and check if they match
        elif lst and char == brackets_dict[lst[-1]]:
            lst.pop()

        # If the character is not a bracket or if it does not match the expected closing bracket --> invalid string
        else:
            return False

    # If the list is empty, all opening brackets have been matched and the input string is valid
    return len(lst) == 0


print(is_valid("()[]{}"))

# --- CODE EXPLANATION --- #

