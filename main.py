from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong arcade game')
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# keys function
screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

game_is_on = True

while game_is_on:
  
    # update screen
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()
    
    # collision with side walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.changing_ball_direction_y()
    
    # collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.changing_ball_direction_x()
        
    # missing paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_paddle_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_paddle_score()

screen.exitonclick()
