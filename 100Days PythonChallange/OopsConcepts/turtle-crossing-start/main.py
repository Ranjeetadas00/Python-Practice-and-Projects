import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

ply1 = Player()
cars = CarManager()
sboard = Scoreboard()
screen.listen()
screen.onkey(ply1.moveUp,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # ply1.moveUp()
    cars.create_car()
    cars.car_move()
    

    # for detecting collision with the car
    for car in cars.allcars:
        if car.distance(ply1)<20:
            game_is_on = False
            sboard.game_over()

    #detecting end finishng line
    if ply1.finish_line():
        ply1.go_to_Start()
        cars.level_up()
        print(f"car speed is {cars.level_up()}")
        sboard.sooreboard_level()


screen.exitonclick()


