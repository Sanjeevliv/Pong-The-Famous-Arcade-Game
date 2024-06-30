from turtle import *
from paddle import Paddle
from ball import Ball
import time
from score_board import ScoreBoard

sc=Screen()
sc.setup(height=600, width=800)
sc.bgcolor("black")
sc.title("Pong Game")
sc.tracer(0)

r_paddle=Paddle((380,0))
l_paddle=Paddle((-380,0))
ball=Ball()
scoreboard= ScoreBoard()

sc.listen()
sc.onkey(r_paddle.go_up, "Up")
sc.onkey(r_paddle.go_down, "Down")
sc.onkey(l_paddle.go_up, "w")
sc.onkey(l_paddle.go_down, "s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()
    

    if ball.ycor()>270 or ball.ycor()<-270:
        ball.ybounce() 

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 360) or (ball.distance(l_paddle) < 50 and ball.xcor() < -360):
        ball.xbounce()

    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_score_update()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_score_update()
    

sc.exitonclick()