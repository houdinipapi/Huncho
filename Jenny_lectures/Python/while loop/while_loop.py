# Simple while loop function
count = 1

# while count <= 5: print(count); count += 1
while count <= 5:
    print(count)
    count += 1

    # Terminating the loop forcefully
    if count == 3:
        break
else:
    print("In ELSE block")
print("Out of loop")

# Exiting a while loop using a sentinel value i.e., special value
number = int(input("Enter a number: (-1 to quit)"))
while number != -1:
    print(number)
    number = int(input("Enter a number: (-1 to quit)"))
else:
    print("ELSE")
print("WE OUTSIDE!!!")