from turtle import *

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score=0
        self.r_score=0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 260)
        self.write(self.l_score, align="center", font=("Arial", 24, "normal"))
        self.goto(100, 260)
        self.write(self.r_score, align="center", font=("Arial", 24, "normal"))

    def l_score_update(self):
        self.l_score +=1
        self.update_scoreboard()

    def r_score_update(self):
        self.r_score +=1
        self.update_scoreboard()
