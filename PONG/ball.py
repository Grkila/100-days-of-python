from turtle import Turtle
import random
class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        if abs(self.ycor())>280:
            self.bounce_y()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.1

    def new_ball(self,pravac):
        self.setpos(0,0)
        if pravac=="left":
            self.x_move = -3
            self.y_move = random.randint(-3,0)

        if pravac=="right":
            self.x_move = 3
            self.y_move = random.randint(0,3)