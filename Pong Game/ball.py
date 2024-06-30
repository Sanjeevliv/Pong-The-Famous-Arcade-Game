from turtle import Turtle


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("grey")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.move_speed=0.001

    def move(self):
        new_x= self.xcor() + self.x_move
        new_y= self.ycor() + self.y_move
        self.goto(new_x,new_y)

    
    def ybounce(self):
        self.y_move *= -1
        self.move_speed * 0.1

    def xbounce(self):
        self.x_move *= -1
        self.move_speed * 0.1

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.xbounce()