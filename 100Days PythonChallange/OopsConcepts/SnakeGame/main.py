from turtle import Turtle,Screen
from snake import Snake
from food import Food
import time
from score import ScoreBord


sc = Screen()
sc.setup(width = 600, height=600)
sc.bgcolor("light green")
sc.title("My Snake Game ")
# ini_snake_pos_x = [0,-20,-40]
# seg = []

food = Food()
scoreboard = ScoreBord()
snake_obj = Snake()
sc.listen()
sc.onkey(key="Up" , fun = snake_obj.up)
sc.onkey(key="Down" , fun = snake_obj.down)
sc.onkey(key="Left" , fun = snake_obj.left)
sc.onkey(key="Right" , fun = snake_obj.right)
# sc.onkey("Down" , down)
# sc.onkey("Left", left)
# sc.onkey("Right" , right)

sc.tracer(0)
game_on = True
# for i in range(3):
    # new_turtle = Turtle("square")
#     new_turtle.penup()
#     new_turtle.goto(ini_snake_pos_x[i],0)
#     seg.append(new_turtle)


while game_on:
    sc.update()
    time.sleep(0.1)
    snake_obj.move()

    # detecting collision with food
    if snake_obj.head.distance(food) < 15:
        # print("YUM YUm Yum")
        food.refresh_food()
        snake_obj.extend()
        scoreboard.increase_score()
        

    # Detectng Collision with wall
    if snake_obj.head.xcor()>280 or snake_obj.head.xcor()<-280 or snake_obj.head.ycor()<-295 or snake_obj.head.ycor()>295:
        game_on=False
        scoreboard.game_over()


    #Detect collision with tail.
    for segment in snake_obj.seg:
        if segment == snake_obj.head:
            pass
        elif snake_obj.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    
    # for i in range(len(seg)-1 , 0 , -1):
    #     new_x = seg[i-1].xcor()
    #     new_y = seg[i-1].ycor()
    #     seg[i].goto(new_x,new_y)
    #     # i.fd(20)
    # seg[0].fd(20)
    # seg[0].left(90)    
        

sc.exitonclick()