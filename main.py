# import all files we need
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# screen requirements
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Guriela's Snake Game")
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
screen.tracer(0)

# our main objects
my_snake = Snake()
food = Food()
scoreboard = Scoreboard()

# functions to play with arrows
screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")

# main game loop
game_is_on = True
while game_is_on:
    screen.update()
    my_snake.move()
    time.sleep(0.1)

    # detect collision with the food
    if my_snake.head.distance(food) < 17:
        food.refresh()
        scoreboard.increase_score()
        my_snake.extend()
    # detect collision with the wall
    if my_snake.head.xcor() > 295 or my_snake.head.xcor() < -300 or my_snake.head.ycor() > 300 or my_snake.head.ycor() < -300:
        scoreboard.reset()
        my_snake.reset()

    # detect collision with the tail
    for segment in my_snake.snake[1:]:
        if my_snake.head.distance(segment) < 10:
            scoreboard.reset()
            my_snake.reset()

screen.exitonclick()
