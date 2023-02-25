#!/usr/bin/python3

print("Welcome to Houdini Safaris!!")
age = int(input("How old are you? "))
person_sharing = int(input("How many people are sharing the room? "))

if age >= 18:
    print("You can book a room.")
    if person_sharing <= 1:
        bill = 150
        print("Your bill will be $150.")
    elif person_sharing <= 3:
        bill = 250
        print("Your bill will be $250.")
    else:
        bill = 350
        print("Your bill will be $350.")

    room_services = input("Would you like in-room services(Y/N)? ")
    if room_services == 'y' or room_services == 'Y':
        bill += 50
        print(f"Your bill will be ${bill}")
else:
    print("You cannot book a room")
print("Thank you!!")
