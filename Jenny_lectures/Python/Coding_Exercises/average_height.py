# Taking user Input
user_heights = input("Enter your heights separated with a space:\n")
heights_list = user_heights.split()
print(heights_list)

# Finding the length of the list
heights = 0
for i in heights_list:
    heights += 1
print(heights)

# Converting the elements into integers
for i in range(heights):
    heights_list[i] = int(heights_list[i])
print(heights_list)

# Calculating the sum of the numbers in the list
total = 0
for personal_height in heights_list:
    total += personal_height
print("The total is: ", total)

# Finding the average
avg = round(total / heights)
print("Average height is: ", avg)
