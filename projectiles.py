from turtle import Turtle
import random


class Projectiles:

    def __init__(self, player, invaders):
        self.player_missiles = []
        self.invader_missiles = []

        self.player = player
        self.invaders = invaders
        self.missile_speed = 12

    def player_shoot(self):
        missile = Turtle(shape="arrow")
        missile.color(240, 255, 240)
        missile.setheading(90)
        missile.shapesize(stretch_wid=0.5, stretch_len=0.5)
        missile.penup()
        missile.goto(self.player.xcor(), self.player.ycor() + 10)
        self.player_missiles.append(missile)

    def invader_shoot(self):
        random_invader = random.choice(self.invaders.invaders)

        invader_missile = Turtle(shape="arrow")
        invader_missile.color(50, 205, 50)
        invader_missile.turtlesize(stretch_wid=0.5, stretch_len=0.5)
        invader_missile.setheading(270)
        invader_missile.penup()
        invader_missile.goto(random_invader.xcor(), random_invader.ycor() - 10)
        self.invader_missiles.append(invader_missile)

    def move_missile(self):
        for missile in self.player_missiles:
            missile.goto(missile.xcor(), missile.ycor() + self.missile_speed)
            if missile.ycor() > 350:
                self.player_missiles.remove(missile)

        for missile in self.invader_missiles:
            missile.goto(missile.xcor(), missile.ycor() - self.missile_speed)
            if missile.ycor() < -350:
                self.invader_missiles.remove(missile)

    def hit_target(self, missile):
        missile.hideturtle()

        if missile in self.player_missiles:
            self.player_missiles.remove(missile)
        else:
            self.invader_missiles.remove(missile)
