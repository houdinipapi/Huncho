"""
A program that replaces specific word.
"""


def word_replacement():
    statement = "Hi, I am a self-taught programmer."
    print(statement)
    word_to_replace = input("Enter a word to replace: ")
    new_word = input("Enter the replacement: ")

    return statement.replace(word_to_replace, new_word)


word_replacement()
