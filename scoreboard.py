from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", font=FONT)

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.goto(-225, 250)
        self.write(f"Level {self.score}", font=FONT)

