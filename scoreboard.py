from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-120, 260)
        self.level = 1
        self.update()

    def level_up(self):
        self.level +=1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="right", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=FONT)