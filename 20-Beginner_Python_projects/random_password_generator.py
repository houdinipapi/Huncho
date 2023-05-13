"""
Random password generator.
"""
import random

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_+=-[]{};':<>,.?/"

while True:
    password_len = int(input("Password length: "))

    if password_len == 0:
        quit()

    else:
        password_count = int(input("How many passwords: "))
        for paswd in range(0, password_count):
            password = ""

            for character in range(0, password_len):
                password_char = random.choice(char)
                password += password_char

            print(f"Password: {password}")

        print("\n")
