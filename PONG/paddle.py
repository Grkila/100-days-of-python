from turtle import Turtle
class Paddle(Turtle):

    def __init__(self,mode):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=20/20,stretch_wid=100/20)
        self.speed("fastest")
        if mode=="right":
            self.goto(x=350,y=0)
        elif mode=="left":
            self.goto(x=-350,y=0)


    def up(self):

        if self.ycor()>=250:
            return
        self.goto(self.xcor(),self.ycor()+20)

    def down(self):
        if self.ycor()<=-250:
            return
        self.goto(self.xcor(),self.ycor()-20)

