import random
import turtle as t
"""import colorgram

rgb_colors=[]
colors=colorgram.extract("image.jpg",30)

for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    rgb_colors.append((r,g,b))

print(rgb_colors)"""

color_list=[ (202, 164, 110),(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


screen=t.Screen()



tim=t.Turtle()
t.colormode(255)
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
tim.hideturtle()
tim.speed(10)
number_of_dots=10
for i in range(number_of_dots):
    for j in range(number_of_dots):
        tim.dot(20,random.choice(color_list))
        if(j!=9):
            tim.forward(50)
    if i%2==0:
        tim.left(90)
        tim.fd(50)
        tim.left(90)
    else:
        tim.right(90)
        tim.fd(50)
        tim.right(90)

screen.exitonclick()
