from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.hideturtle()
        self.pencolor("black")
        self.penup()
        self.color("black")
        self.update_score()

    def update_score(self):
        self.clear()
        self.draw_finish_line()
        self.goto(-260, 240)
        self.player_score += 1
        self.write(f"Level {self.player_score}", font=FONT, align="left")

    def end_of_game(self):
        self.clear()
        self.draw_finish_line()
        self.goto(0, 0)
        self.write(f"GAME OVER\nYou reached Level {self.player_score}", font=FONT, align="Center")

    def draw_finish_line(self):
        self.goto(-290, 280)
        self.pendown()
        self.seth(0)
        while self.xcor() < 300:
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
        self.penup()
