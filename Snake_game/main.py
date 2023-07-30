from turtle import Screen
import time
import snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

jimmy=snake.Snake(screen)
food=Food()
board=Scoreboard()
screen.listen()
screen.onkey(jimmy.up,key="Up")
screen.onkey(jimmy.down,key="Down")
screen.onkey(jimmy.left,key="Left")
screen.onkey(jimmy.right,key="Right")

game_is_on=True

while game_is_on:
    jimmy.move()
    time.sleep(0.1)

    #detect collison with food
    if jimmy.head.distance(food)<15:
        print("nom nom nom")
        food.IsEaten()
        jimmy.extend()
        board.point_won()

    if abs(jimmy.head.xcor()) >280 or abs(jimmy.head.ycor())>280:
        print("Game over")
        game_is_on=False
        board.game_over()
    for part in jimmy.snake_parts[1:]:

        if jimmy.head.distance(part) <10:
            game_is_on=False
            board.game_over()


screen.exitonclick()