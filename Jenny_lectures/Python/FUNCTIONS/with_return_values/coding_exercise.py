def name_formatter(first_name, last_name):
    if first_name == "" or last_name == "":
        return  # Returns None
    else:
        return f"First name: {first_name.title()}\nLast name: {last_name.title()}"


f_name = input("First name: ")
l_name = input("Last name: ")

print(name_formatter(f_name, l_name))