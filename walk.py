# generate a random walk
import turtle as t
import random

tim = t.Turtle()

directions = [1, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

5
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
