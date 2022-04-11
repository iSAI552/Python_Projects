from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 270)
        self.color("blue")
        self.level = 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def inc_level(self):
        self.level += 1
        self.update()

    def over(self):
        self.color("red")
        self.penup()
        self.hideturtle()
        self.home()
        self.write("Game Over", align="left", font=FONT)


