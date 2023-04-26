# filter through the list and give even numbers
numbers = [2, 3, 5, 8, 6, 5, 3, 4, 10]
print("EVEN NUMBERS: ")
print([num for num in numbers if num % 2 == 0])

# map through the list and double each item in the list
print("DOUBLED NUMBERS: ")
print([num * 2 for num in numbers])

# filter through the list and give odd numbers
print("ODD NUMBERS: ")
print([num for num in numbers if num % 2 != 0])

# map through the list and give the next 2 numbers after the current number
print("THE SECOND NUMBER AFTER THE CURRENT: ")
print([num + 2 for num in numbers])
