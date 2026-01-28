import turtle as t
import random

tim = t.Turtle()
colours = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown', 'cyan', 'magenta']

directions = [0, 90, 180, 270]
tim.forward(30)
tim.pensize(15)
tim.speed("fastest")

screen = t.Screen()
screen.exitonclick()

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
