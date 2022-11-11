from turtle import Turtle, Screen
from random import choice
import turtle

tim = Turtle()
tim.shape("turtle")
tim.color("#957DAD")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed('fastest')

for _ in range(200):
    tim.color(choice(colors))
    tim.forward(30)
    tim.setheading(choice(directions))


screen = Screen()
screen.exitonclick()







