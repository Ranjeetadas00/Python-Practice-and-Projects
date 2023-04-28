from turtle import Turtle, Screen

timmy_turtle = Turtle()
timmy_turtle.shape("turtle")
timmy_turtle.color("red")
# timmy_turtle.fd(100)
# timmy_turtle.rt(90)
# timmy_turtle.fd(100)
# timmy_turtle.rt(90)
# timmy_turtle.fd(100)
# timmy_turtle.rt(90)
# timmy_turtle.fd(100)

for _ in range(4):
    timmy_turtle.fd(100)
    timmy_turtle.rt(90)

# timmy_turtle.pendown()
    
for _ in range(10):
    timmy_turtle.fd(10)
    timmy_turtle.pendown()
    timmy_turtle.fd(10)
    timmy_turtle.penup()

screen= Screen()
screen.exitonclick()


