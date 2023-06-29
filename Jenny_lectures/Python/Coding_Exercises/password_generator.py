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

for _ in range(1, (n_letters + 1)):
    char = random.choice(p_letters)
    password += char

print(f"Password: {password}")