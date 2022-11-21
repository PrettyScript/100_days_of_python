from turtle import Turtle, Screen
import pandas

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
# print(val)

guessed_states = []

# # TODO When user gets answer correct the name is placed on respective state


while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?"
    ).title()

    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        # val = state_data[state_data.state == answer_state].iloc[0]["x_y_coordinates"]
        state = Turtle()
        state.hideturtle()
        state.penup()
        # state.goto(val)
        data = state_data[state_data.state == answer_state]
        state.goto(int(data.x), int(data.y))
        # state.write(data.state.item())  # Another way to get the raw data
        state.write(answer_state)
        # answer_state = screen.textinput(title=f"{score}/50 Correct", prompt="What's another state's name?")


screen.exitonclick()
