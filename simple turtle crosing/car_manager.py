from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        super().__init__()
        self.CARS=[]

    def make_car(self):


        if random.randint(1,6)==1:
            car=Turtle()
            car.shape("square")
            car.penup()
            x_start=random.randint(300,1200)
            y_start=random.randint(-240,240)
            car.goto(x_start,y_start)

            car.shapesize(stretch_len=2,stretch_wid=1)
            car.color(random.choice(COLORS))
            self.CARS.append(car)

    def move(self):
        for car in self.CARS:
            car.goto(car.xcor()-STARTING_MOVE_DISTANCE,car.ycor())


    def update_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE+=MOVE_INCREMENT