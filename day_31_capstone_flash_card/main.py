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
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    random_card = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_card)
    canvas.itemconfig(card_background, card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
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

new_image = PhotoImage(file="./images/card_back.png")
old_image = PhotoImage(file="./images/card_front.png")


next_card()

window.mainloop()
