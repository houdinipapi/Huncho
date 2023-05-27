"""
- Implement a program that prompts the user for a fraction, formatted as X/Y,
wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer,
how much fuel is in the tank.
- If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
- And if 99% or more remains, output F instead to indicate that the tank is essentially full.

- If, though, X or Y is not an integer, X is greater than Y, or Y is 0,
instead prompt the user again.
- (It is not necessary for Y to be 4.)
- Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""

while True:
    user = input("Fraction: ")
    try:
        x, y = user.split("/")
        output = round((int(x) / int(y)) * 100)
        if output > 100:
            continue
        else:
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
if output >= 99:
    print("F")
elif output <= 1:
    print("E")
else:
    print(f"{output}%")
