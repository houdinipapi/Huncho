"""
count words if given a string
return the number of words
"""


def count_words(phrase: str) -> int:
    new_list = phrase.split()
    print(new_list)

    return len(new_list)


print(count_words("Today is Monday"))
