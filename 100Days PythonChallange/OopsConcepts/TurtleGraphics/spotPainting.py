from turtle import Turtle, Screen
import turtle
from random import randint 

turtle.colormode(255)


sc=Screen()

def random_color():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    # colors=()
    random_color=(r,g,b)
    return random_color


turtle1 = Turtle()
turtle1.begin_fill()

turtle1.setheading(90+270//2)
turtle1.pu()
turtle1.forward(300)
turtle1.setheading(0)

def turn_left():
    turtle1.setheading(180)
    turtle1.fd(50)
    circular_fills()
    draw_one_row()
    # turn_top()
    # turn_right()

def turn_top():
    turtle1.setheading(90)
    turtle1.fd(50)
    # turn_left()

def turn_right():
    turtle1.setheading(0)
    turtle1.fd(50)
    # turn_top()
    # turn_left()




# turtle1.color("black", "red")
def circular_fills():
    # turtle1.color(random_color())
    # turtle1.begin_fill()
    # turtle1.circle(10)
    # turtle1.end_fill()
    turtle1.dot(20,random_color())

# for i in range(11):
#     turtle1.penup()
#     turtle1.fd(10)
#     turtle1.pendown()
#     turtle1.fd(10)
#     circular_fills()


def draw_one_row():
    for i in range(11):
        
        # turtle1.pendown()
        # turtle1.fd(10)
        circular_fills()
        turtle1.penup()
        turtle1.fd(50)

for i in range(5):
    draw_one_row()
    turn_top()
    turn_left()
    # draw_one_row()
    turn_top()
    turn_right()
    # draw_one_row()
    # turn_right()
    # turn_top()



sc.exitonclick()
