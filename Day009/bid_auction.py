import os
from subprocess import call
from time import sleep
from art import logo

print(logo)

bidding_finished = False
bids = {}


def clear_console():
    _ = call("clear" if os.name == "posix" else "cls")


def find_highest_bid(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


# TODO-1: Ask user for input
while not bidding_finished:
    name = input("What is your name?: ")
    bid_price = int(input("What is your bid price?: $"))
    bids[name] = bid_price

    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n"
    ).lower()
    if should_continue == "no":
        bidding_finished = True
        print("Auction is closed.")
        find_highest_bid(bids)
    elif should_continue == "yes":
        print("Next bidder please.")
        sleep(0.2)
        clear_console()

# TODO-2: Save data to dictionary {name: price} - THIS WAS IN THE WRONG PLACE
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
