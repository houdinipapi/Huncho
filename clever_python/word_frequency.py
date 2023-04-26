"""
Returns the frequency of words in a phrase using dictionaries
>>> word_frequency("Hello Papi")
{'Hello': 1, 'Papi': 1}
"""


def word_frequency(phrase: str) -> dict:
    result = {}
    words = phrase.split()

    for word in words:
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1

    return result


print(word_frequency("Hello There Hello There hello there"))
