alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(message, shift_key):
    cipher_text = ""
    for char in message:
        if char in alphabet:
            # Finding position of the letter in the alphabet list
            index_position = alphabet.index(char)
            # Assigning new position by adding the shift key
            new_position = (index_position + shift_key) % 26
            # Accessing the letter in the new position
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Encrypted message:\n{cipher_text}")


def decryption(cipher_text, shift_key):
    message = ""
    for char in cipher_text:
        if char in alphabet:
            index_position = alphabet.index(char)
            new_position = (index_position - shift_key) % 26
            message += alphabet[new_position]
        else:
            message += char
    print(f"Decrypted message:\n{message}")


#flag
stop = False

while not stop:
    # Ask user what to do:
    task = input("Type 'encrypt' for encryption, type 'decrypt' for decryption.\n").lower()
    user_message = input("Type your message:\n").lower()
    shift = int(input("Enter shift key: "))

    if task == "encrypt":
        encryption(message=user_message, shift_key=shift)
    elif task == "decrypt":
        decryption(cipher_text=user_message, shift_key=shift)
    continue_play = input("Type 'yes' to continue and 'no' to exit: ")
    if continue_play == 'no':
        stop = True
        print("GOODBYE!!")
    