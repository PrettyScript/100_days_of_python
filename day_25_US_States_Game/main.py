import turtle
import pandas
import State

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pandas.read_csv("50_states.csv")
states = state_data.state.tolist()

state = State()


# print(states)
score = 0
correct_states = []

quiz_on = True
# TODO When user gets answer correct the name is placed on respective state

while quiz_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    
    if answer_state in states:
        # print(True)
        score += 1
        correct_states.append(answer_state)
        # answer_corr_x = state_data[state_data.state == answer_state].x
        # answer_corr_y = state_data[state_data.state == answer_state].y
        # print(state_data[state_data.state == answer_state].y)
        state.penup()
        state.goto(220, -145)
        state.write(f"{answer_state}")        
        # print(f"1st: {answer_state}")
        #The title of the text input is keeping track of the user's progress i.e. 4/50 Correct
        answer = turtle.textinput(title=f"{score}/50 Correct", prompt="What's another state's name?")
        if answer in states:
            correct_states.append(answer)
            print(f"2nd: {answer}")
    # TODO If the user gets it incorrect then they are prompted again
    else:
        quiz_on = False
        print("You Lose.")
        turtle.write("You Lose!")

    print(correct_states)

# turtle.mainloop()
screen.exitonclick()
