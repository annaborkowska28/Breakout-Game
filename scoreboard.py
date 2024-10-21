from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=200, y=-250)
        self.score = 0
        self.lives =1
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.write(f'Score: {self.score}, Lives: {self.lives}')

    def add_score(self):
        self.score += 1
        self.update_scores()

    def decrease_lives(self):
        self.lives -= 1
        self.update_scores()

    def reset(self):
        self.clear()
        self.update_scores()
        self.goto(x=200, y=-270)
        self.write(f'Your score is: {self.score}')
