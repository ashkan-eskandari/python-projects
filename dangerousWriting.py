from tkinter import *
from datetime import datetime

counter = 10
running = False


def count():
    global counter
    global running
    if running:
        tt = datetime.fromtimestamp(counter)
        string = tt.strftime("%S")
        label['text'] = string

    if counter < 1:
        text.delete('1.0', END)
        label['text'] = "Start Again..."
        running = False
    label.after(1000, count)
    counter -= 1


def key_press(e):
    global counter
    counter = 10


def key_released(e):
    global running
    global counter
    if running:
        counter = 10
    if not running:
        running = True
        count()


root = Tk()
root.title("Dangerous Writing")

frame = Frame(root, width=250, height=250)
root.bind('<KeyPress>', key_press)
root.bind('<KeyRelease>', key_released)

root.config(padx=50, pady=50)
label = Label(frame, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack()
f = Frame(root)

text = Text(frame, width=100, height=20)
text.config(pady=20, padx=20, )
text.pack()
text.focus()
frame.pack(anchor='center', pady=5)

root.mainloop()
