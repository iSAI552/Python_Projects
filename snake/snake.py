from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.pieces = []
        self.create_snake()
        self.head = self.pieces[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_pieces(position)

    def add_pieces(self, position_to_add):
        piece = Turtle("square")
        piece.color("white")
        piece.penup()
        piece.goto(position_to_add)
        self.pieces.append(piece)

    def extend(self):
        self.add_pieces(self.pieces[-1].position())

    def move(self):
        for piece_num in range(len(self.pieces) - 1, 0, -1):
            new_x = self.pieces[piece_num - 1].xcor()
            new_y = self.pieces[piece_num - 1].ycor()
            self.pieces[piece_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for piece in self.pieces:
            piece.goto(1000, 1000)
        self.pieces.clear()
        self.create_snake()
        self.head = self.pieces[0]
