"""
>>> roman_to_int('VII')
7
>>> roman_to_int('X')
10
"""

# -- EXPLANATION -- #
# - The function uses a dictionary to map each Roman numeral to its corresponding integer value.
# - It then loops through the input string, adding or subtracting values from the result as needed
# - based on the Roman numeral rules.


def roman_to_int(s: str) -> int:
    """
    Convert a Roman numeral string to an integer
    :param s: 'IX'
    :return: 9
    """
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # --> Initialize the result
    result = 0

    # --> Loop through the string, adding values to the result
    for i in range(len(s)):
        # --> If the current letter is the last letter, add its value to the result
        if i == len(s) - 1:
            result += roman_values[s[i]]

        # --> Otherwise, check if the current letter should be subtracted
        else:
            if roman_values[s[i]] < roman_values[s[i+1]]:
                result -= roman_values[s[i]]
            else:
                result += roman_values[s[i]]

    return result


print(roman_to_int('XXX'))
