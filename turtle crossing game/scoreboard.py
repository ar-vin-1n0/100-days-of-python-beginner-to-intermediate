from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-350,250)
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Arial",20, "normal"))




    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", font=("Arial", 15, "normal"), align="center")


    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
