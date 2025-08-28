print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want?\n S, M or L: ")
peperoni = input("Do you want pepperoni in your pizza?\n Y or N: ")
extra_cheese = input("Do you want extra cheese?\n Y or N: ")

# todo: work out how much they need to pay based on their size choice
bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("You didn`t choose Pizza Size.")
# todo: work out how much to add to their bill based on their pepperoni choice.

if peperoni == "Y":
    if size == "S":
        bill += 2
else:
    bill += 3
# todo: work out their final amount based on whether if they want extra cheese

if extra_cheese == "Y":
    bill += 1
else:
    print("Your Pizza will be without Extra Cheese.")

print(f"Your final bill is: ${bill}.")
