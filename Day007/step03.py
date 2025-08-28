import random
from hangman_word_list import word_list
from hangman_art import logo, stages

# Initial Game Congiguration:
number_of_attemps = 6
word_list = word_list
# print(word_list)

print(logo)

choosen_word = random.choice(word_list)
# print(choosen_word)

# Print placeholders for choosen word
placeholder = ""
word_lenght = len(choosen_word)
for position in range(word_lenght):
    placeholder += "-"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print("##########_Welcome to Hangman_##########")
    guess = input("Guess a letter: ").lower()

    if guess in choosen_word and guess not in correct_letters:
        correct_letters.append(guess)

    display = ""
    for letter in choosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

# Main game loop
    if guess not in choosen_word:
        number_of_attemps -= 1
        print(f"You have {number_of_attemps} attempts left.")
        if number_of_attemps == 0:
            game_over = True
            print("##########_You lose :(_##########")
            print(f"The word was {choosen_word}")

    if "_" not in display:
        game_over = True
        print("You win!")
        print(f"The word was {choosen_word}")

    print(stages[number_of_attemps])
