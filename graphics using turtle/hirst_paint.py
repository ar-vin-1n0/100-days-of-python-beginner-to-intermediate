import colorgram as cg
import random

from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.colormode(255)
screen.setup(width=800, height=600)



rgb = [(196, 165, 120), (141, 81, 59), (219, 201, 140), (63, 94, 120), (162, 150, 55), (140, 162, 178), (127, 36, 26), (69, 37, 32), (54, 114, 89), (188, 97, 82), (146, 177, 152), (21, 91, 72), (33, 58, 75), (225, 177, 168), (162, 145, 158), (110, 74, 77), (181, 204, 175), (91, 146, 127), (155, 15, 21), (14, 70, 57), (180, 91, 94), (42, 66, 86), (37, 75, 83), (113, 127, 147), (174, 198, 203), (108, 6, 9)]

t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)
t.pendown()

t.speed(0)

t.hideturtle()
for i in range(10):
    for j in range(10):

        t.pendown()
        t.dot(20,random.choice(rgb))
        t.penup()
        t.forward(50)

    t.backward(500)
    t.left(90)
    t.forward(50)
    t.right(90)

screen.exitonclick()


