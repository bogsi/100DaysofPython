print(r'''
###############################################################
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
###############################################################
     ''' )
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("You're at a crossroad. Do you want to go left or right? \n").lower()
if choice1 == "left":
    choice2 = input("You've come to a lake. Do you want to swim or wait for a boat? \n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at a house with three doors. " \
        "One red, one yellow, and one blue. Which color do you choose? \n").lower()
        if choice3 == "yellow":
            print("You found the treasure! You win! \n")
        elif choice3 == "red":
            print("It's a room full of fire. Game over. \n")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over. \n")
        else:
            print("You chose a door that doesn't exist. Game over. \n")
    else:
        print("You got attacked by an angry trout. Game over. \n")
else:
    print("You fell into a hole. Game over.")
