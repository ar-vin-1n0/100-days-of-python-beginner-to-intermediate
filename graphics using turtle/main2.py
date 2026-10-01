
from turtle import Screen,Turtle
import random

screen = Screen()
t = Turtle()
t.speed(0)
screen.colormode(255)

def random_color():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    rand_color = ( r, g, b)
    return rand_color

for i in range(1000):
    t.color(random_color())
    t.circle(100)
    t.tiltangle(2)
    t.left(2)


screen.exitonclick()