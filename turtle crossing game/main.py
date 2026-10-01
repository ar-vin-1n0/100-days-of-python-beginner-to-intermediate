from turtle import Screen
import time

from avatar import Avatar
from cars import Car
from scoreboard import Scoreboard


screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("turtle crossing game")


avatar = Avatar()

screen.onkey(avatar.move_forward, "w")
screen.onkey(avatar.move_backward, "s")
screen.listen()

cars = Car()
scoreboard = Scoreboard()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    cars.create_car()
    cars.move()

    for car in cars.all_cars:
       if car.distance(avatar) < 20:
          game_on = False
          scoreboard.game_over()

    if avatar.ycor() > 280:
        scoreboard.increase_level()
        avatar.goto_start()
        cars.level_up()






screen.exitonclick()

