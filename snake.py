from turtle import Screen, Turtle

MOVE_POSITION = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.x_pos = 0
        self.no_turtles = 3
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in POSITION:
            self.add_seg(position)

    def add_seg(self, position):
        luci = Turtle("square")
        luci.penup()
        luci.goto(position)
        luci.color("white")
        self.segments.append(luci)

    def extend(self):
        self.add_seg(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(x=new_x, y=new_y)

        self.head.forward(MOVE_POSITION)

    def reset(self):
        for seg in self.segments:
           seg.goto(800, 800)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def collide(self):
        if self.head.xcor == -280 or self.head.xcor == 280 or self.head.ycor == -280 or self.head.ycor == 280:
            return True

    def game_end(self):
        return False
