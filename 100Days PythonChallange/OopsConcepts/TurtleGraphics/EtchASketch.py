from turtle import Turtle,Screen

tim =Turtle()
sc = Screen()

def move_Forward():
    tim.forward(20)

def move_back():
    tim.back(20)

def turn_right():
    tim.right(45)

def turn_left():
    tim.left(45)

def clear_everything():
    tim.clear()
    tim.home()
    

sc.listen()
sc.onkey(key="w",fun=move_Forward)
sc.onkey(key="s",fun=move_back)
sc.onkey(key="c",fun=turn_right)
sc.onkey(turn_left,"a")

# tim.fd(15)
# tim.right(25)

# tim.color('red', 'yellow')
# tim.begin_fill()
# while True:
#     tim.forward(200)
#     tim.left(170)
#     if abs(tim.pos()) < 1:
#         break
# tim.end_fill()
# tim.done()
sc.exitonclick()