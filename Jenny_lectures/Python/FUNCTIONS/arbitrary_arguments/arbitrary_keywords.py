def info_person(**kwargs):  # Ke-worded arguments
    for key, value in kwargs.items():  # Accessing the keys & values --> As dictionaries.
        print(key, value)

info_person(name="Jay", age=45, dept="CSE")
info_person(name="Chulo", school="ALX")

# EXERCISE #
def multiply(*args):
    prod = 1
    for i in args:
        prod *= i
    return prod

print(multiply(4, 5, 6, 7))