from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)  # Adjust the y-coordinate to position the text
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)  # Adjust the y-coordinate to position the text
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def add_score(self, paddle):
        if paddle == "left":
            self.l_score += 1
            self.clear()
            self.update_scoreboard()
        elif paddle == "right":
            self.r_score += 1
            self.clear()
            self.update_scoreboard()
