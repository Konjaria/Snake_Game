import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    user_defined_level = "slow"

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def Left(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.head.setheading(180)

    def Right(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.head.setheading(0)

    def add_segment(self, position):
        new_snake = turtle.Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.speed(self.user_defined_level)
        new_snake.goto(position)
        self.segments.append(new_snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())
