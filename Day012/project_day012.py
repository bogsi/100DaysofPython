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
from random import randint

def get_difficulty_level():
    level_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level_choice == "easy":
        return 10
    elif level_choice == "hard":
        return 5
    else:
        print("Invalid Choice! Defaulting to easy.")
        return 10

def get_user_guess():
    while True:
        try:
            user_input = input("Enter a number between 1 and 100 (or 'quit' to exit): ")
            if user_input.lower() == 'quit':
                return None
            return int(user_input)
        except ValueError:
            print("Please enter a valid number!")

def check_guess(guess, target, attempts_left):
    if guess > target:
        print("Too high.")
        return attempts_left - 1
    elif guess < target:
        print("Too low.")
        return attempts_left - 1
    else:
        print(f"You guessed it! The number was {target}")
        return attempts_left

def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    rand_num = randint(1, 100)
    print("I am thinking of a number between 1 and 100. ")
    
    attempts_left = get_difficulty_level()
    
    while attempts_left > 0:
        guessed_number = get_user_guess()
        
        if guessed_number is None:
            print("Thanks for playing!")
            break
            
        if guessed_number == rand_num:
            print(f"You guessed it! The number was {rand_num}")
            break
            
        attempts_left = check_guess(guessed_number, rand_num, attempts_left)
        
        if attempts_left > 0:
            print(f"You have {attempts_left} attempts left")
    
    if attempts_left == 0:
        print(f"You lose! The number was {rand_num}")

play_game()
