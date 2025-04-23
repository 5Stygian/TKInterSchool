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

questionTitle = [
    "Question 1",
    "Question 2 ([x,y])",
    "Question 3",
    "Question 4 (power rule)",
    "Question 5 (True/False)"
]

answers = [
    "3",
    "[-7,-4]",
    "26",
    "5x^4 + -4x^-3",
    "false"
]

def main():
    global score, question
    question = 1
    user_input = entry.get().lower().strip()

    # Increment question number
    #question += 1

    # Check answers based on the current question
    match question:
        case 1:
            if user_input == answers[0]:
                score += 1
                question += 1
                scoreLabel.config(text = f"Score: {score}")
        case 2:
            if user_input == answers[1]:
                score += 1
                question += 1
                scoreLabel.config(text = f"Score: {score}")
        case 3:
            if user_input == answers[2]:
                score += 1
                question += 1
                scoreLabel.config(text = f"Score: {score}")
        case 4:
            if user_input == answers[3]:
                score += 1
                question += 1
                scoreLabel.config(text = f"Score: {score}")
        case 5:
            if user_input == answers[4]:
                score += 1
                question += 1
                scoreLabel.config(text = f"Score: {score}")

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
        scoreLabel.place_forget()
        entry.place_forget()
        button.place_forget()

        if score == 5:
            win.config(bg="#3aba5c")
            winLabel.place(x = 400, y = 300)
        else:
            win.config(bg="#c72e33")
            lossLabel.place(x = 400, y = 300)
            scoreLabel.place(x = 400, y = 250)
            restart.place(x = 400, y = 350)

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
    text = questionTitle[0],
    fg   = "black",
    bg   = "white",
    font = ("Arial", 24, "bold")
)
q2 = Label(
    text = questionTitle[1],
    fg   = "black",
    bg   = "white",
    font = ("Arial", 24, "bold")
)
q3 = Label(
    text = questionTitle[2],
    fg   = "black",
    bg   = "white",
    font = ("Arial", 24, "bold")
)
q4 = Label(
    text = questionTitle[3],
    fg   = "black",
    bg   = "white",
    font = ("Arial", 24, "bold")
)
q5 = Label(
    text = questionTitle[4],
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

winLabel = Label(
    text = "You got 5/5!",
    fg   = "black",
    bg   = "white",
    font = ("Arial", 24, "bold")
)

lossLabel = Label(
    text = "You loose :(",
    fg   = "black",
    bg   = "white",
    font = ("Arial", 24, "bold")
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

restart = Button(
    win, 
    text    = "Restart",
    bg      = "wheat",
    fg      = "red", 
    width   = 5,
    height  = 2,
    command = main
)

main()
win.mainloop()
