import random
from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)   #10x10 size circle
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)    #the food goes to new random location
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

