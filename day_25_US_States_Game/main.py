from turtle import Turtle, Screen
import pandas

# import State

screen = Screen()
turtle = Turtle()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
state_data["x_y_coordinates"] = list(zip(state_data.x, state_data.y))
states = state_data.state.tolist()
val = state_data[state_data.state == "Florida"].iloc[0]["x_y_coordinates"]
print(val)


# print(states)
score = 0
correct_states = []
state = Turtle()
state.hideturtle()

quiz_on = True
# TODO When user gets answer correct the name is placed on respective state

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

while quiz_on:

    if answer_state in states:
        score += 1
        correct_states.append(answer_state)
        val = state_data[state_data.state == answer_state].iloc[0]["x_y_coordinates"]
        state.hideturtle()
        state.penup()
        state.goto(val)
        state.write(f"{answer_state}")
        answer_state = screen.textinput(title=f"{score}/50 Correct", prompt="What's another state's name?")
    else:
        quiz_on = False
        print("You Lose.")
        turtle.write("You Lose!")

    print(correct_states)


screen.exitonclick()
