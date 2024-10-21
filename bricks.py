from turtle import Turtle
import random

COLOR_LIST = ['blue', 'green', 'yellow', 'purple', 'red', 'pink', 'blue']
WEIGHTS = [1, 2, 1, 1, 3, 2, 1, 4, 1, 3,
           1, 1, 1, 4, 1, 3, 2, 2, 1, 2,
           1, 2, 1, 2, 1]
class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color(random.choice(COLOR_LIST))
        self.goto(x=x_cor, y=y_cor)
        self.quantity = random.choice(WEIGHTS)

        # Defining borders of the brick
        self.left_wall = self.xcor() - 10
        self.right_wall = self.xcor() + 10
        self.upper_wall = self.ycor() + 5
        self.bottom_wall = self.ycor() - 5

class Bricks:
    def __init__(self):
        self.y_start = 20
        self.y_end = 250
        self.bricks = []
        self.create_all_lanes()

    def create_lane(self, y_cor):
        for i in range(-350, 350, 33):
            brick = Brick(i, y_cor)
            self.bricks.append(brick)

    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 42):
            self.create_lane(i)
