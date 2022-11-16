from turtle import Turtle


class Barriers:

    def __init__(self):
        self.positions = []
        self.barriers = []

        self.create_positions()
        self.set_barriers()

    def create_positions(self):
        x, y = -270, -200
        for row in range(3):
            for col in range(4):
                self.positions.append((x + (col * 20), y + (row * 20)))
                self.positions.append((x + 120 + (col * 20), y + (row * 20)))
                self.positions.append((x + 240 + (col * 20), y + (row * 20)))
                self.positions.append((x + 360 + (col * 20), y + (row * 20)))
                self.positions.append((x + 480 + (col * 20), y + (row * 20)))

    def set_barriers(self):
        for pos in self.positions:
            self.create_barrier(pos)

    def create_barrier(self, position):
        new_barrier = Turtle(shape="square")
        new_barrier.color(50, 205, 50)
        new_barrier.penup()
        new_barrier.goto(position)
        self.barriers.append(new_barrier)

    def destroy_barrier(self, barrier):
        barrier.hideturtle()
        self.barriers.remove(barrier)
