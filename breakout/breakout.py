import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from blocks import Blocks
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=500, height=700)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -300))
blocks = Blocks()
ball = Ball((0, -270))
blocks.create_blocks()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

#
#
game_is_on = True
while game_is_on:
    time.sleep(0.07)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() > 220 or ball.xcor() < -220:
        ball.bounce_y()

    # Detect collision with roof
    if ball.ycor() > 310:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -270:
        ball.bounce_x()
    # Detect collision with blocks
    for block in blocks.all_blocks:
        if ball.distance(block) < 40:
            ball.bounce_x()
            block.goto(x=900, y=900)
            scoreboard.point()
    # Detect paddle misses the ball
    if ball.ycor() < -320:
        ball.hideturtle()
        scoreboard.lost()
        break
    #  Detect win
    check_for_win = all(block.position() == (900, 900) for block in blocks.all_blocks)
    if check_for_win:
        ball.hideturtle()
        paddle.hideturtle()
        scoreboard.win()
        break

screen.exitonclick()
