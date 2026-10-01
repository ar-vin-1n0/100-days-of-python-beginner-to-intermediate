from turtle import Turtle

TURTLE_DEFAULT = (0,-280)

class Avatar(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.setheading(90)
        self.goto(TURTLE_DEFAULT)

    def move_forward(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def move_backward(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def goto_start(self):
        self.goto(TURTLE_DEFAULT)



