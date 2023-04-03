user_heights = input("Enter your heights separated with a space:\n")
heights_list = user_heights.split()
print(heights_list)
heights = 0

for i in heights_list:
    heights += 1
print(heights)

for i in range(heights):
    heights_list[i] = int(heights_list[i])
print(heights_list)

total = 0
for personal_height in heights_list:
    total += personal_height
print("The total is: ", total)

avg = round(total / heights)
print("Average height is: ", avg)
