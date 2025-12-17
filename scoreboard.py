from turtle import Turtle

FONT = ("Courier",24,"noramal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-210,250)
        self.write(arg=f"Level = {self.level}", align="center", font=("Courier", 20, "bold"))

    def update_score(self):
        self.level+=1
        self.clear()
        self.write(arg=f"Level = {self.level}", align="center", font=("Courier", 20, "bold"))