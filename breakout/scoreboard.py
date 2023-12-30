from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 240)
        self.write(self.score, align="center", font=("Courier", 65, "normal"))


    def point(self):
        self.score += 1
        self.update_scoreboard()
    def lost(self):
        self.clear()
        self.goto(0, 240)
        self.write(f"you lost! score:{self.score}", align="center", font=("Courier", 35, "normal"))
    def win(self):
        self.clear()
        self.goto(0, 0)
        self.write("YOU WIN!", align="center", font=("Courier", 50, "normal"))