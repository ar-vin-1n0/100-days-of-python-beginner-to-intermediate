import time
from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import  Scoreboard



screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)

screen.bgcolor("black")
screen.title("Ping Pong")


l_paddle_position = (-350,0)
l_paddle = Paddle(l_paddle_position)

r_paddle_position = (350,0)
r_paddle = Paddle(r_paddle_position)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()

scoreboard = Scoreboard()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()


    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()


    #Right paddle
    if ball.xcor()  >370 :
        ball.reset()
        scoreboard.r_point()

    #left paddle
    if ball.xcor() < -370:
        ball.reset()
        scoreboard.l_point()

screen.exitonclick()