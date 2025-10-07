# Import Random module
import random
# Import art
from art import logo, vs
# Import game data
from game_data import  data
# Logic for formatting data and return printable format
def format_data(account):
    """Takes the account data and returns the printable format."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"
# Some logic for count of correct answers and if wrong display final count of correct answers
def check_answers(guess, a_followers, b_followers):
    """Takes the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
# Display art, null scores, game_continue
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Some logic for comparison who has more followers
while game_should_continue:
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # Check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answers(guess, a_follower_count, b_follower_count)
    
    # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
