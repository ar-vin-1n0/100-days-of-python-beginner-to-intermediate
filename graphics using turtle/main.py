from turtle import Turtle, Screen
import random

t = Turtle()

colors = ["red", "green", "blue", "yellow", "cyan", "magenta","black"]

screen = Screen()
for j in range(3,10):
    angle = 360 // j
    t.color(random.choice(colors))
    for i in range(1,j+1):
        t.right(angle)
        t.forward(100)

screen.exitonclick()




