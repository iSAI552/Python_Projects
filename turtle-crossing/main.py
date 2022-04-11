import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)
count = 0

tim = Player()
all_cars = []
for _ in range(20):
    car = CarManager()
    all_cars.append(car)
screen.listen()
scoreboard = Scoreboard()
screen.onkey(fun=tim.move, key="Up")
game_is_on = True
while game_is_on:
    time.sleep(all_cars[0].pace)
    screen.update()
    count += 1
    for _ in all_cars:
        _.move_car()

    if count % 6 == 0:
        car = CarManager()
        car.locate()
        all_cars.append(car)

    for car in all_cars:
        if tim.distance(car) < 20:
            game_is_on = False
            scoreboard.over()

    if tim.ycor() > 280:
        tim.go_start_line()
        all_cars[0].inc_pace()
        scoreboard.inc_level()

screen.exitonclick()