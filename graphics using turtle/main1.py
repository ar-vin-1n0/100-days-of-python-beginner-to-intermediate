from turtle import Screen,Turtle
import random

screen = Screen()
t = Turtle()
t.pensize(10)
t.speed(0)

colors = ["red", "green", "blue", "yellow", "cyan", "magenta","black"]
directions = [0,90,180,270]


for _ in range(100):
    t.color(random.choice(colors))
    for _ in range(random.randint(1,4)):
        t.forward(50)
        t.setheading(random.choice(directions))









screen.exitonclick()