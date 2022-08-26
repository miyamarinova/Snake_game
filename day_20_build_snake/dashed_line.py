
from turtle import Turtle, Screen
screen = Screen()
turtle = Turtle()
screen.tracer(0)
for i in range(5):
    turtle.forward(1+1*i)
    turtle.right(45)
screen.tracer(n= 1, delay = 5)
for i in range(5,10):
    turtle.forward(1+1+i)
    turtle.right(45)
screen.update()

screen.tracer(0)
for i in range(10,15):
    turtle.forward(1+1*i)
    turtle.right(45)
screen.update()
screen.tracer(n=1, delay=5)
for i in range(15,20):
    turtle.forward(1+1+i)
    turtle.right(45)



screen.exitonclick()