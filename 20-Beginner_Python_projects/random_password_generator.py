"""
Random password generator.
"""
import random
import string

# --- PART 1 --- #
# char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890`~!@#$%^&*()_+=-[]{};':<>,.?/"
#
# while True:
#     password_len = int(input("Password length: "))
#
#     if password_len == 0:
#         quit()
#
#     else:
#         password_count = int(input("How many passwords: "))
#         for paswd in range(0, password_count):
#             password = ""
#
#             for character in range(0, password_len):
#                 password_char = random.choice(char)
#                 password += password_char
#
#             print(f"Password: {password}")
#
#         print("\n")


# --- PART 2 --- #
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    new_password = ''.join(random.choice(characters) for _ in range(length))
    return new_password


print(f"New Password: {generate_password()}")
