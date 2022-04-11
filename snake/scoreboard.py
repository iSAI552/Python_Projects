from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.color("white")
        self.penup()
        self.goto(x=0, y=280)
        self.score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.score += 1

    def reset(self):
        if self.score - 1 > self.high_score:
            self.high_score = self.score - 1
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.game_over()
        # self.refresh()

    def game_over(self):
        self.home()
        self.write(arg="Game Over!!", align=ALIGNMENT, font=FONT)
