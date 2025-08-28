# TODO-1 Randomly choose a word from a list and put  in variable selected_word
from random import randint, choice
import hangman_art
import hangman_word_list

print(hangman_art.logo)

word_list = hangman_word_list.word_list
choosen_word = choice(hangman_word_list)
print(choosen_word)

# TODO-2 Ask the user to guess a letter from the word. Assing to variable. Lowercase
placeholder = ""
word_lenght = len(hangman_word_list.word_list)
for position in range(choosen_word):
        placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower

# TODO-3 If letter is not part of the word, print a message and do not add it to the list
display  = ""
for letter in choosen_word:
        if letter == guess:
                display += letter
        else:
                display += "_"

# TODO-6 Print the current state of the word with guessed letters revealed and unguessed letters as underscores

# TODO-7 Repeat steps 2-6 until the user has guessed all letters in the word or has made a certain number of incorrect guesses
