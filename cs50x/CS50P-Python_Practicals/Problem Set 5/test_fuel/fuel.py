def main():
    while True:
        user = input("Fraction: ")
        try:
            percentage = convert(user)
            grade = gauge(percentage)
            print(grade)
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("X and Y must be integers")
    if y == 0:
        raise ZeroDivisionError("Y cannot be zero")
    if x > y:
        raise ValueError("X cannot be greater than Y")

    output = round((x / y) * 100)
    return output


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
