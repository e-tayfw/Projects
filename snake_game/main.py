from turtle import Turtle, Screen


# Screen Initialisation
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_seg = Turtle("square")
    new_seg.color('white')
    new_seg.goto(position)

screen.exitonclick()
