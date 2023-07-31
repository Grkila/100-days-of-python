from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.goto(-200,260)
        self.level=0
        self.write_level()

    def update(self):
        self.level+=1
        self.clear()
        self.write_level()

    def write_level(self):
        self.write(f"Level : {self.level}",align="center",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align='center',font=FONT)