# import colorgram
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []

# # for color in range(len(colors)):
# #     r = colors[color].rgb.r
# #     g = colors[color].rgb.g
# #     b = colors[color].rgb.b
# #     rgb_colors.append((r,g,b))

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
from turtle import Turtle, Screen
import turtle
from random import choice
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

timmy = Turtle()
turtle.colormode(255)


# print(timmy.position())
timmy.penup()
# timmy.setposition(-200.0, 0.0)
# timmy.setx(-200)
# timmy.sety(0)
# set_y = 0

for _ in range(10):
    # set_y += 50
    # timmy.setx(-200)
    # timmy.sety(set_y)
    timmy.pendown()
    timmy.dot(20, choice(color_list))
    timmy.penup()
    timmy.forward(50)

# timmy.penup()
# timmy.setposition(-200.0, 50.0)
# for _ in range(10):
#     timmy.pendown()
#     timmy.dot(20, choice(color_list))
#     timmy.penup()
#     timmy.forward(50)








screen = Screen()
screen.exitonclick()


