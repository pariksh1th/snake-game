from turtle import Turtle
import random as r


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.speed("slow")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.refresh()
        # self.position


    def refresh(self):
        self.goto(x=r.randint(-280, 280), y=r.randint(-280, 280))
