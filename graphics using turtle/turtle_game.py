import turtle
from turtle import Turtle,Screen
import random
from tkinter import messagebox

is_on = False

screen = Screen()
screen.setup(width=800,height=600)

user_bet = screen.textinput("turtle bet","Enter ur bet")

colors = ["red","orange","yellow","green","blue","purple"]
y_pos = [-150,-100,-50,0,50,100]

turtles = []

for i in range(0,6):
    shibu = Turtle("turtle")
    shibu.color(colors[i])
    shibu.penup()
    shibu.goto(-380,-y_pos[i])
    turtles.append(shibu)

if user_bet:
    is_on = True

while is_on:
    for t in turtles:
        if t.xcor() == 360:
            is_on = False
            if user_bet == t.pencolor():
                print("u won the bet")
            else:
                print("u loose the bet")
        distance = random.randint(1,10)
        t.forward(distance)

screen.exitonclick()