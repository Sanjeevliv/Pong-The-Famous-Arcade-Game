from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("grey")
        self.penup()
        self.speed("fastest")
        self.setpos(position)

    def go_up(self):
        y=self.ycor() +20
        self.sety(y)

    def go_down(self):
        y=self.ycor() -20
        self.sety(y)

    
    

        

