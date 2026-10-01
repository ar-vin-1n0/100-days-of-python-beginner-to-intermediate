from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("score.txt", "r") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.show_score()


    def show_score(self):
        self.clear()
        score = f"Score: {self.score} High Score: {self.high_score}"
        self.write(arg=score, font=("Arial", 15, "normal"), align="center")


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.show_score()


    def increase_score(self):
        self.score += 1
        self.show_score()


