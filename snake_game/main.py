from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Screen Initialisation
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


game_is_on = True
snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


delay = 0.2

while game_is_on:
    screen.update()
    time.sleep(delay)
    snake.move()

    # Detect collision with food

    if snake.head.distance(food) < 15:
        print("Nom Nom Nom")
        food.refresh()
        delay = delay / 1.10
        scoreboard.add_score()
        snake.extend_snake()
        # game_is_on = False

    # Detect collision with wall
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        scoreboard.reset()
        snake.reset()
        delay = 0.2
        

    # Detect collision with own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            delay = 0.2
            


screen.exitonclick()
