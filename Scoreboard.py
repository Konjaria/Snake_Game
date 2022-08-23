from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
FILE_DIRECTORY = "data.txt"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        high_score = open(FILE_DIRECTORY)
        self.score = 0
        self.high_score = int(high_score.read())
        high_score.close()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILE_DIRECTORY,mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
