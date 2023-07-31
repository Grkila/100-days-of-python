import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
cars=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.make_car()
    cars.move()
    if player.to_start():
        scoreboard.update()
        cars.update_speed()

    for car in cars.CARS:

        if abs(car.xcor()-player.xcor())<30 and abs(car.ycor()-player.ycor())<20:
            game_is_on=False
            scoreboard.game_over()

    screen.update()

screen.exitonclick()