
from turtle import Screen,Turtle

class Snake:
    def __init__(self,screen):
        self.screen=screen
        self.snake_parts = []
        for i in range(0, 3):
            self.add_segment((-20 * i,0))

        self.screen.update()
        self.head=self.snake_parts[0]

    def move(self):
            self.screen.update()
            for seg_num in range(len(self.snake_parts) - 1, 0, -1):
                pos = self.snake_parts[seg_num - 1].xcor(), self.snake_parts[seg_num - 1].ycor()
                self.snake_parts[seg_num].goto(pos)

            self.snake_parts[0].forward(20)

    def add_segment(self,positon):
        new_snake_part = Turtle()
        new_snake_part.shape("square")
        new_snake_part.color("white")
        new_snake_part.penup()
        new_snake_part.setpos(positon)
        self.snake_parts.append(new_snake_part)

    def extend(self):
        self.add_segment(self.snake_parts[-1].position())


    def up(self):
        if self.snake_parts[0].heading()!=270:
            self.snake_parts[0].setheading(90)

    def down(self):
        if self.snake_parts[0].heading()!=90:

            self.snake_parts[0].setheading(270)
    def left(self):
        if self.snake_parts[0].heading()!=0:

            self.snake_parts[0].setheading(180)
    def right(self):
        if self.snake_parts[0].heading()!=180:

            self.snake_parts[0].setheading(0)



