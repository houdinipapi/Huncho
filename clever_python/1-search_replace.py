#!/usr/bin/python3

my_list = []

n = int(input("Enter number of elements: "))

for i in range(0, n):
    element = int(input("Enter an item for the list: "))

    my_list.append(element)

print(my_list)
