from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position) :
        super().__init__()
        self.color("white")
        self.shape("square")
        #by default a turtle is 20 X 20 but for a rectangle of hight 100 and lenght=20 , change stretch_wid = 5(i.e. 5X20=100) and stretch_len = 1(Because we need 20 in x direction)
        self.shapesize(stretch_wid= 5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self):
        new_y_cor = self.ycor()+ 20
        self.goto(self.xcor(), new_y_cor)


    def move_down(self):
        new_y_cor = self.ycor()- 20
        self.goto(self.xcor(), new_y_cor)