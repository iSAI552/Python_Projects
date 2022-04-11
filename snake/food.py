from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_cordi = random.randint(-280, 280)
        y_cordi = random.randint(-280, 280)
        self.goto(x=x_cordi, y=y_cordi)
