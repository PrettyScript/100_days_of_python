from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("#957DAD")

# for _ in range(4):
#     tim.forward(200)
#     tim.right(90)

for _ in range(20):
    tim.pendown()
    tim.forward(10)
    tim.penup()
    tim.forward(10)















screen = Screen()
screen.exitonclick()