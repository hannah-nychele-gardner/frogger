from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1

    def write_level(self):
        self.setposition(-275, 250)
        self.clear()
        self.write(arg=f"Level {self.level}", font=FONT, align="left")

    def write_game_over(self):
        self.setposition(0, 0)
        self.write(arg="GAME OVER", font=FONT, align="center")
