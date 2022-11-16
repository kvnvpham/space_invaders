from turtle import Turtle


class Invaders:

    def __init__(self):
        self.positions = []
        self.invaders = []

        self.move_speed = 5
        self.descent_speed = 10
        self.direction = "right"

        self.create_positions()
        self.set_invaders()

    def create_positions(self):
        x, y = -270, 300
        for i in range(6):
            self.positions.append((x + (i * 60), y))
            self.positions.append((x + (i * 60), y - 60))
            self.positions.append((x + (i * 60), y - 120))

    def set_invaders(self):
        for pos in self.positions:
            self.create_invaders(pos)

    def create_invaders(self, position):
        new_invader = Turtle(shape="turtle")
        new_invader.color(50, 205, 50)
        new_invader.penup()
        new_invader.setheading(270)
        new_invader.goto(position)
        self.invaders.append(new_invader)

    def move_right(self):
        for invader in self.invaders:
            invader.goto(invader.xcor() + self.move_speed, invader.ycor())

    def move_left(self):
        for invader in self.invaders:
            invader.goto(invader.xcor() - self.move_speed, invader.ycor())

    def move_down(self):
        for invader in self.invaders:
            invader.goto(invader.xcor(), invader.ycor() - self.descent_speed)

    def bump_right_wall(self):
        for invader in self.invaders:
            if invader.xcor() > 300:
                self.move_down()
                return True

    def bump_left_wall(self):
        for invader in self.invaders:
            if invader.xcor() < -300:
                self.move_down()
                return True

    def invader_destroyed(self, invader):
        invader.hideturtle()
        self.invaders.remove(invader)

    def is_invaded(self):
        for invaders in self.invaders:
            if invaders.ycor() <= -125:
                return True
