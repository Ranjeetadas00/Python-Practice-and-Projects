from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.shapesize(0.5,0.5)
        self.refresh_food()
        


    def refresh_food(self):
        x_pos = random.randint(-280,280)
        y_pos = random.randint(-280,280)
        self.goto(x_pos,y_pos)


