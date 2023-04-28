from turtle import Turtle,Screen
# from random import randint
import random

tim=Turtle()

colors=["magenta","dark violet","medium violet red","dark red", "dark green","lime green","light sea green","blue","gold"]
def shape(sides):
    number_of_Sides=sides
    angle=360/number_of_Sides
    for i in range(number_of_Sides):
        tim.fd(100)
        tim.rt(angle)
        # sides +=1

for shape_n in range(3,11):
    tim.color(random.choice(colors))
    shape(shape_n)



screen=Screen()
screen.exitonclick()