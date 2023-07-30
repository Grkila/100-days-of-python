
from  turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()

screen.bgcolor("black")
screen.setup(width=800,height=600)

screen.title("PONG GAME")
screen.tracer(0)
lpad=Paddle("left")
rpad=Paddle("right")
ball=Ball()
scoreboard=Scoreboard()

screen.update()
screen.listen()

screen.onkey(key="Up",fun=rpad.up)
screen.onkey(key="Down",fun=rpad.down)

screen.onkey(key="w",fun=lpad.up)
screen.onkey(key="s",fun=lpad.down)

game_is_on=True

while game_is_on:
    time.sleep(0.05)

    ball.move()
    screen.update()
    if ball.distance(rpad)<50 and ball.xcor()>320:
        ball.bounce_x()
    elif ball.distance(lpad)<50 and ball.xcor()<-320:
        ball.bounce_x()
    if  ball.xcor()>=380:
        ball.new_ball("left")
        scoreboard.point_won("right")
    elif ball.xcor()<=-380:
        ball.new_ball("right")
        scoreboard.point_won("left")

screen.exitonclick()