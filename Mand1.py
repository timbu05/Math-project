import turtle as t
import random

t.pendown()
t.speed(0)
t.hideturtle()
t.screensize(1200,800)
for i in range(100000):
    t.right(random.randint(0,360))
    t.forward(10)

t.exitonclick()