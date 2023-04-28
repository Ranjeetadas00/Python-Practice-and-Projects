from turtle import Turtle

INITIAL_SNAKE_POS =  [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST=20
UP=90
DOWN=270
LEFT=180
RIGHT = 0


class Snake:
    
    def __init__(self):
        self.seg = []
        self.create_snake()
        self.head = self.seg[0]

    def create_snake(self):

        for pos in INITIAL_SNAKE_POS:
            self.add_new_pos(pos)
            # new_turtle = Turtle("square")
            # new_turtle.penup()
            # new_turtle.goto(INITIAL_SNAKE_POS[i],0)
            # self.seg.append(new_turtle)

    def add_new_pos(self, pos):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.goto(pos)
        self.seg.append(new_turtle)
    

    def extend(self):
        # add new segment to turtle/slake
        self.add_new_pos(self.seg[-1].position())

    def move(self):
        for i in range(len(self.seg)-1 , 0 , -1):
            new_x = self.seg[i-1].xcor()
            new_y = self.seg[i-1].ycor()
            self.seg[i].goto(new_x,new_y)
            # i.fd(20)
        self.seg[0].fd(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.seg[0].setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.seg[0].setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.seg[0].setheading(180)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.seg[0].setheading(0)


