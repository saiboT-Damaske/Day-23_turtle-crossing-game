from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.generate_car()

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            c1 = Turtle()
            c1.shape("square")
            c1.color(COLORS[random.randint(0, 5)])
            c1.turtlesize(stretch_wid=1, stretch_len=2)
            c1.penup()
            c1.goto(300, random.randint(-250, 250))
            c1.seth(180)
            self.cars.append(c1)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def cars_level_up(self):
        self.car_speed += MOVE_INCREMENT



