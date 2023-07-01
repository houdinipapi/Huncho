def addition(a, b):
    total = a + b
    return total

print(addition(5, 4))  # ans = addition(5, 4) and the print(ans)


# Formatting Name
def format_name(f_name, l_name):
    new_first = f_name.title()
    new_last = l_name.title()
    return f"{new_first}, {new_last}"

print(format_name("Julio", "CAESAR"))