from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=250)
window.config(padx=100, pady=50)


def calculate():
    miles = int(input.get())
    km = miles * 1.609344
    label_3.config(text=km)


input = Entry(width=10)
input.grid(column=2, row=1)

label = Label(text="Miles")
label.grid(column=3, row=1)

label_2 = Label(text="is equal to")
label_2.grid(column=1, row=2)

label_3 = Label(text="0")
label_3.grid(column=2, row=2)

label_4 = Label(text="Km")
label_4.grid(column=3, row=2)

button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=3)

window.mainloop()
