# A script that generates password randomly.
import random
import string

p_letters = string.ascii_letters
p_digits = string.digits
p_punc = string.punctuation

n_letters = int(input("No. of letters: "))
n_digits = int(input("No. of digits: "))
n_punc = int(input("Punctuations: "))

password = ""

# Getting letters
for _ in range(1, (n_letters + 1)):
    char = random.choice(p_letters)
    password += char

# Getting digits/numbers
for _ in range(1, n_digits + 1):
    char = random.choice(p_digits)
    password += char

# Getting special characters
for _ in range(1, n_punc + 1):
    char = random.choice(p_punc)
    password += char

# Converting str into a list
password_list = list(password)
print(password_list)

# Shuffling the list
random.shuffle(password_list)

print(password_list)

# Converting the list into a string
pass_str = ""
new_pass = pass_str.join(password_list)
print(new_pass)