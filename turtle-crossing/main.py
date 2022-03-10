import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="w", fun=player.move)

game_is_on = True
while game_is_on:
    scoreboard.write_level()
    car_manager.create_car()
    # move the cars
    car_manager.move()
    # detect player death
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
    # check if player has completed the level
    if player.level_complete():
        car_manager.level_up()
        player.reset_position()
        scoreboard.level += 1
    time.sleep(0.1)
    screen.update()
scoreboard.write_game_over()

screen.exitonclick()
