from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold "))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)
button_2 = Button(text="Another button")
button_2.grid(column=3, row=1)


# Entry (Input)
input = Entry(width=10)
print(input.get())
input.grid(column=4, row=4)

window.mainloop()
