from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.player_reset()

    def player_reset(self):
        self.goto(STARTING_POSITION)
        self.seth(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def player_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
