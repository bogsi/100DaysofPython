def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


if front_is_clear():
    move()
elif wall_in_front():
    turn_right()




while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

"""
follow right edge of maze, turn_right, 
"""
front_is_clear()
    move()
else
    turn_right()
wall_in_front()
wall_on_girht()
front_is_clear()
