# Calculating sum of numbers
sum_num = 0
num = int(input("Enter a number: "))
while num != 0:  # zero will act as a sentinel value ---> the loop will not be exited forcefully.
    sum_num += num
    print(sum_num)
    num = int(input("Enter a number: "))
    # if num == 0 or num == -1:
    #     break
else:
    print("ELSE")
print("EXITED THE LOOP!!")