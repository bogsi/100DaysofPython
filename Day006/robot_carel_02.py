def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


# for step in range(6):
#     jump()

# number_of_hurdels = 6

# while number_of_hurdels > 0:
#     jump()
#     number_of_hurdels -= 1
#     print(number_of_hurdels)

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
