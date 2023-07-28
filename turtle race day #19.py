
from turtle import Turtle,Screen
import random

is_race_on=False

screen=Screen()
screen.setup(width=500,height=400)
colors=["red","orange","blue","pink","purple","green"]
user_bet=screen.textinput(title="make your bet",prompt="Enter a color: ")
print(user_bet)

start_pos=-70
turtles=[]
for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=start_pos)
    start_pos+=30

    turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor()>230:
            print("Zavrsena je trka")
            winner=turtle
            is_race_on=False
            break

if winner.pencolor()==user_bet:
    print("pobedili ste")
else:
    print("izgubili ste")

screen.exitonclick()
