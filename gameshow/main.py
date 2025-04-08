from tkinter import *
from PIL import Image, ImageTk

score = 0

image1 = open("/latex/q1.png")
image2 = open("/latex/q2.png")
image3 = open("/latex/q3.png")
image4 = open("/latex/q4.png")
image5 = open("/latex/q5.png")

win = Tk()

win.config(bg="cornflower blue")
win.geometry("900x600")
win.title("PyGame is a better lib")

def main():
    user_input = entry.get().lower()
    user_input = user_input.strip()


    entry.delete(0, END)  # Clear the entry after retrieving input

entry = Entry(
    win, 
    width = 30
)
entry.place(
    x = 325,
    y = 250
)

label = Label(
    text = "Question 1",
    fg   = "black",
    bg   = "white",
    font = ("Arial", 24, "bold")
)
label.place(
    x = 50,
    y = 20
)

scoreLabel = Label(
    text = f"Score: {score}",
    fg   = "black",
    bg   = "white",
    font = ("Arial", 24, "bold")
)
scoreLabel.place(
    x = 780,
    y = 20
)

button = Button(
    win, 
    text    = "Submit", 
    command = main
)
button.place(
    x = 400,
    y = 300
)

win.mainloop()
