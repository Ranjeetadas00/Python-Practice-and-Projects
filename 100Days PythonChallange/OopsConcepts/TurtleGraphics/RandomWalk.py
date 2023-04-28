import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255)
tim = Turtle()
# tim.pencolor()
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    # colors=()
    random_color=(r,g,b)
    return random_color

# colors=["magenta","dark violet","medium violet red","dark red", "dark green","lime green","light sea green","blue","gold"]


direction=[0,90,180,270]

for i in range(300):
    # tim.color(random.choice(colors))
    tim.color(random_color())
    tim.setheading(random.choice(direction))
    tim.pensize(20)
    tim.forward(30)
    


sc=Screen()
sc.exitonclick()