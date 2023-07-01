phone_num = {
    "Dior": 123,
    "Chanel": 345,
    "Coco": 465,
}

phone_num["Chanel"] = 7854
print(phone_num)

# Another method of creating dictionaries
reg_name = dict([("Papi", 333), ("Robb", 555), ("Elias", 988)])
print(reg_name)

# Using get() method
print(reg_name.get("Papi"))

data = {
    2: "Houdini",
    3: "Papi",
    0: "Chulo"
}

print(data[0])

# Deleting an item from the dictionary --> using del & pop()
del data[0]  # deletes {0: "Chulo"}
print(data)

data.pop(3)  # deletes {3: "Papi"}
print(data)

# Other built-in functions
cities = {
    "Madrid": "Spain",
    "Lisboa": "Portugal",
    "Manchester": "England",
    "Torino": "Italia"
}

# Deleting the last added item
# print(cities.popitem())  # Removes "Torino" from the dictionary

# Clearing all items in the dictionary
# cities.clear()
# print(cities)  # Prints an empty dictionary

# Accessing keys
print(cities.keys())  # Will only print the keys in a list

# Accessing values
print(cities.values())  # returns the values in a list

# Converting a dictionary into a list
print(cities.items())  # A list with tuples

# Keys can also be printed using a for loop
for city in cities:
    print(city)  # Prints keys only
    print(cities[city])  # Prints the values

# Printing keys and values pairs
for city in cities.items():
    print(city)

# Copying dictionaries
new_cities = cities.copy()
print(new_cities)

# Checking length
print(len(new_cities))
