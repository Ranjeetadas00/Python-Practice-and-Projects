from turtle import Turtle

class ScoreBord(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write(f" Score : {self.score} ", align = "center" ,font=("Arial",24,"normal"))
        
        
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f" Score : {self.score} ", align = "center" ,font=("Arial",24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f" Game Over ", align = "center" ,font=("Arial",24,"normal"))

   