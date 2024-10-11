import time
from turtle import Screen

from Food import Food
from Scoreboard import Scoreboard
from Snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My Snake Game 🐍💖")
screen.bgpic("./images/bg.gif")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
# add key controls to control the snake
screen.listen()

screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_left, "Left")
screen.onkeypress(snake.move_right, "Right")


def start_game():
    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with the food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 250 or snake.head.ycor() < -250:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 8:
                game_is_on = False
                scoreboard.game_over()


start_game()

screen.mainloop()
