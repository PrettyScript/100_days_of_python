import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
states = state_data.state.tolist()
# print(states)
score = 0
correct_states = []


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
print(answer_state)

quiz_on = True
# TODO When user gets answer correct the name is placed on respective state

while quiz_on:
    if answer_state in states:
        # print(True)
        score += 1
        correct_states.append(answer_state)
        turtle.textinput(title=f"{score}/50 Correct", prompt="What's another state's name?")
        print(correct_states)

    # TODO The title of the text input is keeping track of the user's progress i.e. 4/50 Correct
    # TODO If the user gets it incorrect then they are prompted again
    else:
        # print("You Lose.")
        turtle.write("You Lose!")
        # quiz_on = False
        # turtle.done()
        # quiz_on = False

turtle.mainloop()
