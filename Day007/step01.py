# word_list = []

# TODO-1 Randomly choose a word from a list and put  in variable selected_word
import random
choosen_word = random.choice(["apple", "banana", "cherry", "date", "elderberry"])
print(choosen_word)

# TODO-2 Ask the user to guess a letter from the word. Assing to variable. Lowercase
guessed_letter = input("Guess a letter: ").lower()

# TODO-3 Check if letter  is partt of the word
for guessed_letter in choosen_word:
    if guessed_letter in choosen_word:
        print(f"Good job! The letter '{guessed_letter}' is in the word.")
    else:
        print(f"Sorry, the letter '{guessed_letter}' is not in the word.")

# TODO-4 If letter is part of the word, add it to the list of guessed letters

# TODO-5 If letter is not part of the word, print a message and do not add it to the list

# TODO-6 Print the current state of the word with guessed letters revealed and unguessed letters as underscores

# TODO-7 Repeat steps 2-6 until the user has guessed all letters in the word or has made a certain number of incorrect guesses

