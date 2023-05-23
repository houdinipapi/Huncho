#!/usr/bin/python3
user_input = input()
user_input = user_input.replace(" ", "***")
print(user_input)

num_list = [1, 2, 3, 4]
for i in num_list:
    if i % 2 == 0:
        i = 'EVEN'
    print(num_list)
