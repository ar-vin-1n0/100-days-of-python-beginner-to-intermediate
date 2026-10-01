from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def forward():
    t.forward(20)
def backward():
    t.backward(20)
def left():
    t.left(20)
def right():
    t.right(20)
def clr_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(fun=forward, key="w")
screen.onkey(fun=backward, key="s")
screen.onkey(fun=left, key="a")
screen.onkey(fun=right, key="d")
screen.onkey(fun=clr_screen, key="c")
screen.exitonclick()
