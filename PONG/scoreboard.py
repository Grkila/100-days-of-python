
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):

        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_left=0
        self.score_right=0
        self.goto(0,220)
        self.update()

    def point_won(self, player):
        if player=="left":
            self.score_left+=1
        elif player=="right":
            self.score_right+=1
        self.clear()
        self.update()

    def update(self):
        self.write(f"Score\n {self.score_left}:{self.score_right}",align="center",font=("arial",20,"bold"))
