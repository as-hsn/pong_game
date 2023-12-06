from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0, 0))
score = Score()

screen.listen ()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(0.05)
    screen.update()
    ball.ball_move()



    if ball.ycor() > 280 or ball.ycor() < -280 :
       ball.y_bounce()

    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    elif ball.xcor() > 380:
        score.left_score()
        ball.reset()

    elif ball.xcor() < -380:
        score.right_score ()
        ball.reset()



screen.exitonclick()