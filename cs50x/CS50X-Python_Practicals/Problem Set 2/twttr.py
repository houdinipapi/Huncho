"""
- Implement a program that prompts the user for a str of text and then
outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""


def remove_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    output = ""

    for char in word:
        if char not in vowels:
            output += char
    return output


def main():
    word = input("Input: ")
    return f"Output: {remove_vowels(word)}"


if __name__ == "__main__":
    print(main())
