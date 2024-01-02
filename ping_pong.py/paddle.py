from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < 250:
            y = self.ycor() + MOVE_DISTANCE
            self.sety(y)

    def down(self):
        if self.ycor() > -250:
            y = self.ycor() - MOVE_DISTANCE
            self.sety(y)

