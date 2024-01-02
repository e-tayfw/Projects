from turtle import Turtle, Screen
import random

# initialise screen
screen = Screen()
screen.setup(width=500, height=400)

# initialise variables
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "pink"]
is_race_on = False
all_turtles = []


# create new turtles
def creating_turtles():
    start_y = -100
    for i in range(6):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape("turtle")
        new_turtle.color(colors[i])
        new_turtle.goto(x=-230, y=start_y)
        all_turtles.append(new_turtle)
        start_y += 40


def start_race():
    global is_race_on
    if user_bet:
        is_race_on = True


def retrieve_winner():
    global is_race_on
    start_race()

    while is_race_on:
        for turtle in all_turtles:
            random_dist = random.randint(0, 10)
            turtle.forward(random_dist)
            if turtle.xcor() >= 230:
                winner_color = turtle.color()[0]
                is_race_on = False
                return winner_color


creating_turtles()
winner_color = retrieve_winner()
if winner_color.lower() == user_bet.lower():
    print(f"You win, the winner is the {user_bet} turtle!")
else:
    print(f"You lose, the winner is the {winner_color} turtle.")


screen.exitonclick()
