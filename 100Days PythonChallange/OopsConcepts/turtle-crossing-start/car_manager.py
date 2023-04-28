from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allcars =[]
        self.car_speed = STARTING_MOVE_DISTANCE

    
    def create_car(self):
        rand_choice = random.randint(1,6)
        if rand_choice==1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            y_pos = random.randint(-250,250)
            new_car.goto(300,y_pos)
            self.allcars.append(new_car)

    def car_move(self):
        for car in self.allcars:
            car.setheading(180)
            car.forward(self.car_speed)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT