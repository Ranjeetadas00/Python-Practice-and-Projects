from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.y_pos = 0
        
    def moveUp(self):
        # self.y_pos = self.ycor()+10
        self.forward(MOVE_DISTANCE)

    def go_to_Start(self):
        if self.finish_line:
            self.goto(STARTING_POSITION)
    
    def finish_line(self):
        if self.ycor()>=FINISH_LINE_Y:
            return True
        else:
            return False
    
