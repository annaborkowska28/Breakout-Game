import turtle as tr
import time
from ball import Ball
from bricks import Bricks
from paddle import Paddle
from scoreboard import Scoreboard



screen = tr.Screen()
screen.title('Breakout Game')
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.tracer(0)


ball = Ball()
paddle = Paddle()
bricks = Bricks()
scoreboard = Scoreboard()
game_on = True
# Create the key bindings
screen.listen()
screen.onkeypress(paddle.go_left, "Left")
screen.onkeypress(paddle.go_right, "Right")
screen.update()


def collision_with_upper_wall():
    if ball.ycor() > 270:
        ball.bounce_y()

def collision_with_side_walls():
    if ball.xcor() < -370 or ball.xcor() > 370:
        ball.bounce_x()

def collision_with_paddle():
    if paddle.xcor() - 100 <= ball.xcor() <= paddle.xcor() + 100 and ball.ycor() <= paddle.ycor() + 20:
        ball.bounce_y()

def collision_with_bottom_wall():
    global game_on
    if ball.ycor() < - 240:
        ball.reset_position()
        scoreboard.decrease_lives()
        if scoreboard.lives == 0:

            scoreboard.reset()
            game_on = False

def collision_with_bricks():
    for brick in bricks.bricks:
        if ball.distance(brick) < 20:
            scoreboard.add_score()
            brick.quantity -= 1
        if brick.quantity == 0:
            brick.clear()
            brick.goto(1000, 1000)
            bricks.bricks.remove(brick)

            # detect collision from left
            if ball.xcor() < brick.left_wall:
                ball.bounce_x()

            # detect collision from right
            elif ball.xcor() > brick.right_wall:
                ball.bounce_x()

            # detect collision from bottom
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce_y()

            # detect collision from top
            elif ball.ycor() > brick.upper_wall:
                ball.bounce_y()


while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    collision_with_upper_wall()
    collision_with_side_walls()
    collision_with_paddle()
    collision_with_bricks()
    collision_with_bottom_wall()

screen.mainloop()