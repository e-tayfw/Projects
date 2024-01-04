import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Randomly generate cars
    if random.randint(1, 6) == 1:
        cars.create_car()
    cars.move_cars()

    # Check for collisions with cars
    for car in cars.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Check if the player reached the top wall
    if player.is_player_at_finish():
        player.go_to_start()
        cars.increase_speed()
        scoreboard.increase_level()


screen.exitonclick()
