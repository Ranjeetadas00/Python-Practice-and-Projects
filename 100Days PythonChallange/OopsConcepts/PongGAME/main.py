from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

sc = Screen()
ball = Ball()
# sc.screensize(canvwidth=800, canvheight=600)
sc.setup(width = 800 , height = 600)
sc.title("PONG Game")
sc.bgcolor("black")
sc.tracer(0)

paddle_right = Turtle()
score = Scoreboard()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))



sc.listen()
sc.onkey(r_paddle.move_up, "Up")
sc.onkey(r_paddle.move_down, "Down")

sc.onkey(l_paddle.move_up, "w")
sc.onkey(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()
    
    #Detecting wall collision
    if ball.ycor()>=280 or ball.ycor()<=-280:
        ball.bounce_y()
    #Detecting collision with the paddels
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x() 

    # Right paddel misses the ball
    if ball.xcor()>=380:
        ball.reset_position()
        score.l_point()

    #Left paddel misses the ball
    if  ball.xcor()<=-380:
        ball.reset_position()
        score.r_point()

sc.exitonclick()