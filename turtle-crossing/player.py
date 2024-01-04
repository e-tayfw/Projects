from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape('turtle')
        self.setheading(90)

    def up(self):
        y = self.ycor() + MOVE_DISTANCE
        self.sety(y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_player_at_finish(self):
        if self.ycor() >= 280:
            return True
        return False

    
        

