"""
Number Guessing Game

A fun Python game where you try to guess a randomly generated number between 1-100.

Game Features:
- Two difficulty levels:
  * Easy: 10 attempts to guess the number
  * Hard: 5 attempts to guess the number
- Interactive hints (too high/too low) after each guess
- Win by guessing correctly or lose when attempts run out

How to play:
1. Choose your difficulty level
2. Enter your guess (1-100)
3. Follow the hints to narrow down the correct number
4. Win by guessing the number before running out of attempts!
"""

import art
import random
print(art.logo)

# Welcome message and difficulity level choice
print("Welcome to the Number Guessing Game!")
rand_num = random.randint(1, 100)
print("I am thinking of a number between 1 and 100. ")
level_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

guessed_number = 0

# Loop for level choice
if level_choice == "easy":
    attemps_left = 10
elif level_choice == "hard":
    attemps_left = 5
else:
    print("Invalid Choice! Defaulting to easy.")
    attemps_left = 10

# While loop with try/catch for ValueError
while attemps_left > 0 and guessed_number != rand_num:
    try:
        user_input = input("Enter a number (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            print("Thanks for playing!")
            break
        guessed_number = int(user_input)

        if guessed_number < 1 or guessed_number > 100:
            print("Please enter a number between 1 and 100!")
            continue
    except ValueError:
        print("Please enter a valid number!")
        continue

    if guessed_number > rand_num:
        print("Too high.")
        attemps_left -= 1
        print(f"You have {attemps_left} attempts left")
    elif guessed_number < rand_num:
        print("Too low.")
        attemps_left -= 1
        print(f"You have {attemps_left} attempts left")
    else:
        print(f"You guessed it! The number was {rand_num}")
        break

# Check for attemps left
if attemps_left == 0 and guessed_number != rand_num:
    print(f"You lose! The number was {rand_num}")
