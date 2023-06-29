import random

word_list = ["apple", "beautiful", "potato"]
lives = 6

# Generating a random word
chosen_word = random.choice(word_list)
# print(chosen_word)

display = []
# Replacing the letters with a dash
for letter in chosen_word:  # for i in range(len(chosen_word))
    display += '_'
print(display)

game_over = False

while not game_over:
    # User guessing
    guessed_letter = input("Guess a letter: ").lower()

    # Comparing the guessed letter and letters in the chosen word.
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)

    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose!!")
    if '_' not in display:
        game_over = True
        print("You Won")
