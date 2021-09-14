from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class ScoreBoard:
    def __init__(self):
        self.tim = Turtle()
        self.score = 0
        with open("high_score.txt", mode="r") as file:
            self.high_score = file.read()
        # self.high_score = 0
        self.tim.color("white")
        self.tim.hideturtle()
        self.tim.penup()
        self.tim.goto(x=0, y=280)
        self.update_board()

    def update_board(self):
        self.tim.clear()
        self.tim.write(f"score = {self.score}   High score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_board()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
        self.score = 0
        self.update_board()
        self.write_score()

    def write_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))


