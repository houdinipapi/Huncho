#!/usr/bin/python3

my_list = []

n = int(input("Enter number of elements: "))

for i in range(0, n):
    element = int(input("Enter an item for the list: "))

    my_list.append(element)

print(my_list)

for i in range(len(my_list)):

    if my_list[i] == 2:
        my_list[i] = 89

    new_list = my_list.copy()

print(new_list)
