from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


'''Solution'''
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = False

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)
    

'''My Solution on creating multiple turtle instances'''
# turtles = [Turtle(shape='turtle') for i in range(6)]

# starting_places = True
# position_y = -100
# index = 0

# while starting_places:
#     turtles[index].penup()
#     turtles[index].color(colors[index])
#     turtles[index].goto(x=-230, y=position_y)
#     if index < 5:
#         index += 1
#         position_y += 50
#     else:
#         starting_places = False



screen.exitonclick()
