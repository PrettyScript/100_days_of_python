import turtle

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)


answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
# TODO When user gets answer correct the name is placed on respective state
# TODO The title of the text input is keeping track of the user's progress i.e. 4/50 Correct
# TODO If the user gets it incorrect then they are prompted again
