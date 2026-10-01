from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(arg=self.l_score, font=("Arial", 60, "normal"), align="center")
        self.goto(100, 200)
        self.write(arg=self.r_score, font=("Arial", 60, "normal"), align="center")

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_score()


