from turtle import Turtle


class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0,240)

        self.update()

    def point_won(self):
        self.score+=1
        self.clear()
        self.update()
    def update(self):
        self.write(f"Score is {self.score}",False,align='center',font=('Arial', 20, 'bold'))

    def game_over(self):
        self.setpos(0,0)
        self.write("GAME IS OVER",align='center',font=('Arial',20,'bold'))