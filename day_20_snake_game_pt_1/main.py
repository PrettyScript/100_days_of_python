#TODO Create a snake body
#TODO Move the Snake
#TODO Control the Snake w/ keyboard controls
#TODO Detect collision with food
#TODO Create a scoreboard
#TODO Detect collision with wall
#TODO Detect collision with tail

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    #Detect collison with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score()


screen.exitonclick()