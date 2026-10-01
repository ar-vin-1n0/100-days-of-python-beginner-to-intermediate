from turtle import Turtle
import random




COLORS_FOR_CARS = [
    "red","blue","green",
    "yellow","orange",
    "purple","pink","brown",
    "cyan","magenta"]

class Car:
    def __init__(self):
        self.all_cars = []
        self.speed = 10


    def create_car(self):

        if random.randint(1, 6) == 1:
            new_car= Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(self.car_color())
            new_car.penup()
            new_car.goto(self.car_position())
            self.all_cars.append(new_car)


    def car_color(self):
        return random.choice(COLORS_FOR_CARS)

    def car_position(self):
        new_x = 400
        new_y = random.randint(-300,300)
        pos = (new_x, new_y)
        return pos


    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)


    def level_up(self):
        self.speed += 10





