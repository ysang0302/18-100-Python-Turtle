import colorgram
import random
import turtle as t

# generate a random color list from pic
rgb_color = []
colors = colorgram.extract('travel.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)

# draw the graph with the random color list
tim = t.Turtle()

t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# move the turtle to the left-down side of the conor
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(rgb_color))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()