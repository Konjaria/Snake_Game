from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Sylvane", 24, 'bold')


class scoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.text = f"Score: {self.score} "
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.write(self.text, False, ALIGNMENT, FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score :  {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(" Game Over ", align=ALIGNMENT, font=FONT)
