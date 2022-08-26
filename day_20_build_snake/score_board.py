from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align = ALIGNMENT, font = FONT)

    def increased_score(self):
        self.score += 1
        self.clear()
        self.update_score()

