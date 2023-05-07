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
"""
- The 'is_valid' function takes a string 's' as an input.
- It first creates a dictionary 'brackets_dict' that maps opening brackets to their corresponding closing brackets.
- An empty list is the created to keep track of the opening brackets.
- The function loops through each character in the input string.
- If the character is an opening bracket, it is pushed onto the list.
- If the character is a closing bracket, we pop the last opening bracket from the list and check if they match.
- If they do not match or if the list is empty, then the input string is invalid and the function returns 'False'.
- After looping, we check if the list is empty.
- If it is empty, then all opening brackets have been matched and the input string is valid.
- If it is not empty, then there are unmatched opening brackets and the input is invalid.
"""
