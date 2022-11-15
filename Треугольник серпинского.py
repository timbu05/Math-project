import turtle
import math

def triangle(x_1,y_1,x_2,y_2,x_3,y_3,kol):
    turtle.pencolor('black')
    turtle.fillcolor('white')
    turtle.pensize(2)
    turtle.penup()
    turtle.setpos(round(x_1), round(y_1))
    turtle.pendown()
    turtle.begin_fill()
    turtle.setpos(round(x_2), round(y_2))
    turtle.setpos(round(x_3), round(y_3))
    turtle.setpos(round(x_1), round(y_1))
    turtle.end_fill()
    if kol > 1:
        triangle((x_1 + (x_1 + x_2) / 2) / 2, (y_1 - (y_3 - y_1) / 2), (x_2 + (x_1 + x_2) / 2) / 2,(y_2 - (y_3 - y_1) / 2), (x_1 + x_2) / 2, y_1, kol - 1)
        triangle((x_2 + x_3) / 2, (y_2 + y_3) / 2, x_2 + (x_2 - x_3) / 2, (y_2 + y_3) / 2, x_2, y_3, kol - 1)
        triangle((x_1-(x_3-x_1)/2),(y_1+y_3)/2,(x_1+x_3)/2,(y_1+y_3)/2,x_1,y_3,kol-1)

kol = int(input())

x_1, y_1 = -200/2-100, -((math.sqrt(3)/2)*200)
x_2, y_2 = 0, 200
x_3, y_3 = 200/2+100, -((math.sqrt(3)/2)*200)

turtle.speed(0)
turtle.hideturtle()
turtle.pensize(5)
turtle.pencolor('black')
turtle.fillcolor('black')
turtle.penup()
turtle.setpos(x_1,y_1)
turtle.pendown()
turtle.begin_fill()
turtle.setpos(x_2, y_2)
turtle.setpos(x_3, y_3)
turtle.setpos(x_1, y_1)
turtle.end_fill()

if kol > 1:
    triangle((x_1 + x_2) / 2, (y_1 + y_2)/ 2, (x_2 + x_3) / 2, (y_2 + y_3)/2, (x_1 + x_3) / 2, (y_1 + y_3) / 2, kol - 1)

turtle.exitonclick()