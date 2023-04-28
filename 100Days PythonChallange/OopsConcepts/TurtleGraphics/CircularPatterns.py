from turtle import Turtle, Screen
import turtle
from random import randint 

turtle.colormode(255)

def random_color():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    # colors=()
    random_color=(r,g,b)
    return random_color


tim = Turtle()
# tim.home()
# tim.heading()
# tim.left(90)
# tim.degrees(360)
size_gap=10
for i in range(360//size_gap):
    tim.pensize(3)
    tim.color(random_color())
    tim.left(10)
    tim.degrees(360)
    tim.circle(100)
    tim.speed("fastest")
    


sc=Screen()
sc.exitonclick()

