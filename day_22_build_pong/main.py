#TODO Create the screen
#TODO Create and move the a paddle
#TODO Create another paddle
#TODO Create the ball and make it move
#TODO Detect collision with wall and bounce
#TODO Detect collision with paddle
#TODO Detect when paddle misses
#TODO Keep Score

from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")


turtle = Turtle()
turtle.color("white")
turtle.shape("square")
# turtle.shapesize(stretch_wid=20, stretch_len=60)
turtle.turtlesize(stretch_wid=5, stretch_len=1)
turtle.penup()
turtle.setpos(350, 0)



def move_up():
    turtle.goto(350, 5)

def move_down():
    turtle.goto(350, -5)

screen.listen(move_up, "Up")
screen.listen(move_down, "Down")





screen.exitonclick()