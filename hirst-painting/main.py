# Extract Colors Required
import colorgram
import turtle as t
import random

rgb_colors = []
colors = colorgram.extract("image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

colors = [
    (202, 164, 109),
    (150, 75, 49),
    (223, 201, 135),
    (52, 93, 124),
    (172, 154, 40),
    (140, 30, 19),
    (133, 163, 185),
    (198, 91, 71),
    (46, 122, 86),
    (72, 43, 35),
    (145, 178, 148),
    (13, 99, 71),
    (233, 175, 164),
    (161, 142, 158),
    (105, 74, 77),
    (55, 46, 50),
    (183, 205, 171),
    (36, 60, 74),
    (18, 86, 90),
    (81, 148, 129),
    (148, 17, 20),
    (14, 70, 64),
    (30, 68, 100),
    (107, 127, 153),
    (174, 94, 97),
    (176, 192, 209),
]

tim = t.Turtle()
t.colormode(255)


tim.penup()
tim.speed('fastest')

starting_y = -250
for _ in range(10):
    tim.goto((-250, starting_y))
    for _ in range(10):
        tim.color(random.choice(colors))
        tim.dot(20)
        tim.fd(50)
    starting_y += 50

tim.hideturtle()


# Initialize Screen
screen = t.Screen()
screen.exitonclick()
