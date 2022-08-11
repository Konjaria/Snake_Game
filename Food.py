import turtle as t
import random as r


class FOOD(t.Turtle):
    def __init__(self):
        super().__init__()
        #self.Score = 0
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("Blue")
        self.speed("fastest")
        random_x = r.randint(-200, 200)
        random_y = r.randint(-200, 200)
        self.goto(random_x, random_y)

    def refresh(self):
        X= r.randint(-200, 200)
        Y = r.randint(-200, 200)
        self.goto(X, Y)


