import re


def main():
    print(count(input("Test: ")))


def count(s):
    """
    - Expects a string and returns an integer
    - Counts the number of times 'um' appears in that text,
    case-insensitively.
    - 'um' should be a word unto itself, not as a sub-string
    of some other word.
    'hello, um, world' --> 1
    'yummy' --> 0
    """
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
