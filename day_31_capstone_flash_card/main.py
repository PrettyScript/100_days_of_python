BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
from random import choice

data_file = pandas.read_csv("./data/french_words.csv")
# french_words = data_file["French"].to_list()
# english_words = data_file["English"].to_list()
# words = data_file.set_index("French")["English"].to_dict()
# random_french_word = choice(french_words)
to_learn = data_file.to_dict(orient="records")


def next_card():
    current_card = choice(to_learn)
    random_card = current_card["French"]
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=random_card)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="./images/right.png")
known_button = Button(image=check_img, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
