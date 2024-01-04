from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('snake_game/data.txt') as data:
            self.high_score = int(data.read())

        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)  # Adjust the y-coordinate to position the text
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=FONT)

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open('snake_game/data.txt', mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
