from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("MY Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #     Detect the collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.refresh()
        snake.extend()

    #     Detect wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    #     Detect collision with the tail
    for parts in snake.pieces[1:]:
        if snake.head.distance(parts) < 10:
            game_on = False
            scoreboard.reset()
            snake.reset()
            # scoreboard.game_over()

screen.exitonclick()
