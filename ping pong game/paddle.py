from turtle import Turtle



class Paddle(Turtle):
    def __init__(self,paddle_position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle_position = paddle_position
        self.create_paddle()

    def create_paddle(self):
        self.goto(self.paddle_position)


    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)


    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)

