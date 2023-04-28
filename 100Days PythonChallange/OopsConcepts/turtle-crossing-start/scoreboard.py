from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.level = 1
        self.goto(-280,250)
        self.update_scoreb0ard()

    def update_scoreb0ard(self):
        self.clear()
        self.write(f"Level :{self.level} " , align="left" , font=FONT)
    
    def sooreboard_level(self):
        self.level+=1
        self.update_scoreb0ard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over" , align="center" , font=FONT)