import time
from turtle import Screen
from player import Player
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()
screen.onkeypress(player.move, "Up")


game_is_on = True
game_loop = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if game_loop % 6 == 0:
        car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    game_loop += 1





screen.exitonclick()