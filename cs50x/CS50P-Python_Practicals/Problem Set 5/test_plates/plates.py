def main():
    plate = input("Plate: ")

    if is_valid(plate):
        return True
    else:
        return False


def is_valid(s):
    length = len(s)

    if 2 <= length <= 6:
        for _ in s:
            if not s.isalnum():
                return False

            elif s[0].isdigit() or s[1].isdigit():
                return False

            elif s[0:2].isalpha():
                middle = s[1:-1]
                if middle.isnumeric() and middle.find(0):
                    break

                zeroIndex = s.find("0") - 1
                if s[-zeroIndex].isdigit():
                    for char in s:
                        if char.isdigit():
                            if char.startswith("0"):
                                return False
                            else:
                                return True

                elif s[-2].isdigit() and s[-1].isalpha():
                    return False

                elif s[-2].isdigit():
                    return True

                elif s[0:2].isalpha():
                    return True

            else:
                return False

    else:
        return False


if __name__ == "__main__":
    print(main())
