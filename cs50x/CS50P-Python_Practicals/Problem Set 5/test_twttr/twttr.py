def main():
    word = input("Input: ")
    print(f"Output: {shorten(word)}")


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    output = ""

    for char in word:
        if char.lower() not in vowels:
            output += char
    return output


if __name__ == "__main__":
    main()
