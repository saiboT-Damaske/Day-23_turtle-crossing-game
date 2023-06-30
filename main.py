import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
score = Scoreboard()
game_is_on = True
cars = CarManager()


screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")
iterator = 1

while game_is_on:
        time.sleep(0.1)
        screen.update()
        cars.generate_car()
        cars.move_cars()

        # detect collision with car
        for car in cars.cars:
            if car.distance(player) < 20:
                game_is_on = False
                score.end_of_game()

        # detect if player reaches other side
        if player.player_at_finish():
            player.player_reset()
            score.update_score()
            cars.cars_level_up()

screen.exitonclick()
