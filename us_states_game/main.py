import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("US States Game")

image = "us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_on = True
data = pd.read_csv("us_states_game/50_states.csv")
 # Check if the user entered a state name
states_list = data.state.to_list()

guessed_states = []



while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title="Guess the State", prompt="What's another state's name? "
    ).title()

    if answer_state == "Exit":
        break
    if answer_state in states_list:
        guessed_states.append(answer_state)
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        state_data = data[data.state == answer_state]
        new_turtle.goto(int(state_data.x), int(state_data.y))
        new_turtle.write(
            f"{answer_state.capitalize()}",
            align="center",
            font=("Arial", 10, "normal"),
        )
    screen.update()

not_guessed = [state for state in states_list if (state.title() not in guessed_states)]
new_data = {
    'States not guessed': not_guessed
}
states_not_guessed_df = pd.DataFrame(new_data)
states_not_guessed_df.to_csv("us_states_game/states_not_guessed.csv")


screen.exitonclick()
