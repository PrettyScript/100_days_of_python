BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

window = Tk()
window.title("Flashy")


canvas = Canvas(width=800, height=530, background=BACKGROUND_COLOR)
front_card_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 250, front_card_img)
canvas.grid(column=1, row=0)


window.mainloop()
