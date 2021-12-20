import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()

    # Detect collision between turtle and car
    if cars.detect_collision(player):
        game_is_on = False
        score.game_over()

    # Detect successful crossing
    if player.ycor() > 275:
        player.reset_player()
        score.update_scoreboard()
        cars.increase_speed()

screen.exitonclick()
