from turtle import Turtle, Screen
# from random import randint
import random

# new_turtle = Turtle(shape="turtle")
# new_turtle2 = Turtle(shape="turtle")
# new_turtle3 = Turtle(shape="turtle")
# new_turtle4 = Turtle(shape="turtle")
# new_turtle5 = Turtle(shape="turtle")
# new_turtle6 = Turtle(shape="turtle")
# new_turtle7 = Turtle(shape="turtle")



sc=Screen()
sc.setup(width=500, height=400)
user_bet = sc.textinput("bet", "What colour turtle You think will win the race ?\n (Enter any Rainbow Colour) \n Red, Orange, Yellow, Green, Blue, Indigo, Violet ")

race_on=True
# new_turtle.goto(-230,-120)
# new_turtle2.goto(-230,-60)
# new_turtle3.goto(-230,-20)
# new_turtle4.goto(-230,160)
# new_turtle5.goto(-230,120)
# new_turtle6.goto(-230,80)
# new_turtle7.goto(-230,20)
turtle_colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo" , "Violet"]
y_pos = [40,80,120,-10,-50,-90,-120]
all_new_turtles=[]

for i in range(1,8):
    new_turtle = Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(turtle_colors[i-1].lower())
    new_turtle.goto(-230,y_pos[i-1])
    all_new_turtles.append(new_turtle)

if user_bet:
    race_on = True
while race_on:

    for turtle_1 in all_new_turtles:
        if turtle_1.xcor()>230:
            winner_Color=turtle_1.pencolor()

            race_on=False
            if(user_bet==winner_Color):
                print(f" You Won!! 🤩, The Winnng turtle is {winner_Color} ")

            else:
                print(f" You Loose 😔!!, The Winnng turtle is {winner_Color} ")
                
        speed=random.randint(1,10)
        turtle_1.fd(speed)





sc.exitonclick()