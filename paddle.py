from turtle import Turtle

MOVE_DISTANCE = 30

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape("square")
        self.shapesize(stretch_len=10)
        self.penup()
        self.goto(x=0, y=-200)
        self.distance = MOVE_DISTANCE

    def go_left(self):
        if self.xcor() > -300:
            self.back(MOVE_DISTANCE)

    def go_right(self):
        if self.xcor() < 300:
            self.fd(MOVE_DISTANCE)