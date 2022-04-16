from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=x_cor, y=y_cor)
    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        if -250 < self.ycor():
            new_y = self.ycor() - 20
            self.goto(x=self.xcor(), y=new_y)





