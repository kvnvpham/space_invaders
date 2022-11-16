import turtle
from turtle import Turtle

START_POS = (0, -275)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color((0, 255, 0))
        self.setheading(90)
        self.penup()
        self.goto(START_POS)

        self.move_speed = 15

    def move_left(self):
        if self.xcor() < -320:
            self.goto(self.xcor(), self.ycor())
        else:
            new_x = self.xcor() - self.move_speed
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() > 320:
            self.goto(self.xcor(), self.ycor())
        else:
            new_x = self.xcor() + self.move_speed
            self.goto(new_x, self.ycor())

    def reset_pos(self):
        self.goto(START_POS)
