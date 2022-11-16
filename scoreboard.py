from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(-335, -330)

        self.score = 0
        self.lives = 3

    def update_score(self):
        self.clear()
        self.pendown()
        self.write(f"Score: {self.score}\n"
                   f"Lives:  {self.lives}",
                   align="left",
                   font=("Arial", 12, "normal"))

    def is_winning(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write("You Win!",
                   align="center",
                   font=("Arial", 20, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write("Game Over",
                   align="center",
                   font=("Arial", 20, "normal"))
