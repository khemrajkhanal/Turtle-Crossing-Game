import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(player.go_up,"Up")



game_is_on=True

while game_is_on:
    time.sleep(0.1)
    car_manager.create_cars()
    car_manager.move_cars()

    screen.update()

    for hit_cars in car_manager.cars:
        if player.distance(hit_cars)<20:
            game_is_on=False
            game_over=Turtle()
            game_over.pen()
            game_over.color("black")
            game_over.write(arg="GAME OVER!",align="center",font=("Courier",40,"bold"))


    if player.is_level_clear():
        player.go_to_start()
        car_manager.level_up()

        scoreboard.update_score()


screen.exitonclick()