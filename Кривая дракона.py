import turtle

def Dragon(x_1,y_1,x_2,y_2,count):
    if count > 0:
        x_n = round((x_1 + x_2) / 2) + round((y_2 - y_1) / 2)
        y_n = round((y_1 + y_2) / 2) - round((x_2 - x_1) / 2)
        Dragon(x_1, y_1, x_n, y_n, count - 1)
        Dragon(x_2, y_2, x_n, y_n, count - 1)

    else:
        turtle.penup()
        turtle.setpos(round(x_1),round(y_1))
        turtle.pendown()
        turtle.setpos(round(x_2), round(y_2))

count = int(input())
turtle.speed(0)
turtle.hideturtle()
turtle.pensize(5)
Dragon(-200,-100,100,-100,count)
turtle.exitonclick()