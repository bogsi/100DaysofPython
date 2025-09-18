import turtle, colorsys

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors = [colorsys.hls_to_rgb(i/36,1,1) for i in range(36)]

for i in range(36):
    t.color(colors[i])
    t.circle(100)
    t.left(10)

turtle.done()
