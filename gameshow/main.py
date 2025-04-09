from tkinter import *
from PIL import Image, ImageTk

score = 0

win = Tk()

win.config(bg="#aaa")
win.geometry("900x600")
win.title("PyGame is a better lib")

image1 = ImageTk.PhotoImage(Image.open("gameshow/latex/q1.png"))
image2 = ImageTk.PhotoImage(Image.open("gameshow/latex/q2.png"))
image3 = ImageTk.PhotoImage(Image.open("gameshow/latex/q3.png"))
image4 = ImageTk.PhotoImage(Image.open("gameshow/latex/q4.png"))
image5 = ImageTk.PhotoImage(Image.open("gameshow/latex/q5.png"))

def main():
    global score, question
    question = 1
    user_input = entry.get().lower().strip()

    # Check answers based on the current question
    if question == 1 and user_input == "3":
        score += 1
    elif question == 2 and user_input == "[-7,-4]":
        score += 1
    elif question == 3 and user_input == "pass":
        score += 1
    elif question == 4 and user_input == "5x^4 + -4x^-3":
        score += 1
    elif question == 5 and user_input == "false":
        score += 1

    # Update the display based on the current question
    if question == 1:
        q1.place(x=50, y=20)
        im1.place(x=350, y=20)
    elif question == 2:
        q1.place_forget()
        im1.place_forget()
        q2.place(x=50, y=20)
        im2.place(x=350, y=20)
    elif question == 3:
        q2.place_forget()
        im2.place_forget()
        q3.place(x=50, y=20)
        im3.place(x=350, y=20)
    elif question == 4:
        q3.place_forget()
        im3.place_forget()
        q4.place(x=50, y=20)
        im4.place(x=350, y=20)
    elif question == 5:
        q4.place_forget()
        im4.place_forget()
        q5.place(x=50, y=20)
        im5.place(x=350, y=20)
    elif question > 5:
        q5.place_forget()
        im5.place_forget()

    # Increment question number
    question += 1

    entry.delete(0, END)  # Clear the entry after retrieving input

entry = Entry(
    win, 
    width = 30
)
entry.place(
    x = 325,
    y = 250
)

q1 = Label(
    text = "Question 1",
    fg   = "black",
    bg   = "white",
    font = ("Arial", 24, "bold")
)
q2 = Label(
    text = "Question 2",
    fg   = "black",
    bg   = "white",
    font = ("Arial", 24, "bold")
)
q3 = Label(
    text = "Question 3",
    fg   = "black",
    bg   = "white",
    font = ("Arial", 24, "bold")
)
q4 = Label(
    text = "Question 4",
    fg   = "black",
    bg   = "white",
    font = ("Arial", 24, "bold")
)
q5 = Label(
    text = "Question 5",
    fg   = "black",
    bg   = "white",
    font = ("Arial", 24, "bold")
)

im1 = Label(win, image = image1)
im2 = Label(win, image = image2)
im3 = Label(win, image = image3)
im4 = Label(win, image = image4)
im5 = Label(win, image = image5)

scoreLabel = Label(
    text = f"Score: {score}",
    fg   = "black",
    bg   = "white",
    font = ("Arial", 24, "bold")
)
scoreLabel.place(
    x = 760,
    y = 20
)

button = Button(
    win, 
    text    = "check answer", 
    command = main
)
button.place(
    x = 400,
    y = 300
)

main()
win.mainloop()
