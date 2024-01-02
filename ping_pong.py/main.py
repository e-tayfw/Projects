from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

game_is_on = True

# Initialise Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # check if the ball hit
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_wall()

    # check if ball collide with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (
        ball.distance(l_paddle) < 50 and ball.xcor() < -320
    ):
        ball.bounce_paddle()

    # check if paddle misses
    if ball.xcor() > 380:
        scoreboard.add_score("left")
        ball.refresh()

    if ball.xcor() < -380:
        scoreboard.add_score("right")
        ball.refresh()


screen.exitonclick()
