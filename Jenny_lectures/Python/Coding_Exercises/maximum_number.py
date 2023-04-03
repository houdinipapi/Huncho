# Taking User Input
numbers_str = input("Enter numbers separated by a space: ")

# Splitting the input into a list
new_numbers_str = numbers_str.split()
print(new_numbers_str)

# Finding length of the list
count = 0
for i in new_numbers_str:
    count += 1
print(count)

# Converting the list elements into integers
for i in range(count):
    new_numbers_str[i] = int(new_numbers_str[i])

print(new_numbers_str)

# Finding the Maximum number in the list
max_num = new_numbers_str[0]
for nums in new_numbers_str:
    if nums > max_num:
        max_num = nums

print(max_num)
