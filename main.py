import time
from turtle import Screen, write, Turtle
from Scoreboard import scoreBoard
from Food import FOOD
from snake import Snake

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenzia")
screen.tracer(0)
# Snake
snake = Snake()
apple = FOOD()
Score = scoreBoard()
Game_Over = Turtle()
Game_Over.hideturtle()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(apple) < 15:
        apple.refresh()
        snake.extend()
        Score.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        Score.game_over()
        game_is_on = False
    #
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         Score.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            Score.game_over()
screen.exitonclick()
