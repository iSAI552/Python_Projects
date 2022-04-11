from turtle import Turtle
from random import randint, choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
INITIAL_PACE = 0.1


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.pace = INITIAL_PACE
        self.setheading(180)
        self.color(choice(COLORS))
        self.goto(x=randint(0, 280), y=randint(-240, 240))

    def move_car(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def locate(self):
        self.goto(x=300, y=randint(-240, 240))

    def inc_pace(self):
        self.pace *= 0.5
