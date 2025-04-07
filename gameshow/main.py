from tkinter import *
from turtle import setpos

win = Tk()

win.config(bg="cornflower blue")
win.geometry("900x600")
win.title("PyGame is a better lib")

class MyButton:
    """
    Args:
        text(str): text displayed on the button
        xPos(int): x position of the button on the TKinter window
        yPos(int): y position of the button on the TKinter window
        xDim(int): length of the button
        yDim(int): width of the button
        bg(str): background color of the button
        fg(str): text color of the button
        setpos(int): sets the button's position to either the left or the right
        correct(bool): set whether the button is correct or not
    """
    def __init__(self, text=None, xPos=None, yPos=None, xDim=None, yDim=None, bg=None, fg=None, setpos=None, correct=None):
        self.text    = text
        self.xPos    = xPos
        self.yPos    = yPos
        self.xDim    = xDim
        self.yDim    = yDim
        self.bg      = bg
        self.fg      = fg
        self.setpos  = setpos
        self.correct = correct
    
    def setposFoo(self):
        if self.setpos == 0:
            self.xPos -= 100
        elif self.setpos == 1:
            self.xPos += 100

    def foo(self):
        if self.correct == True:
            win.config(bg="black")
        elif self.correct == False:
            win.config(bg="white")

button1 = MyButton("button1", 400, 300, 10, 3, "wheat", "red", 0, False)
button1.setposFoo()
button1XPos, button1YPos = button1.xPos, button1.yPos
button1 = Button(
    win,
    text                = button1.text,
    highlightbackground = button1.bg,
    fg                  = button1.fg,
    width               = button1.xDim,
    height              = button1.yDim,
    command             = button1.foo
)
button1.place(
    x = button1XPos,
    y = button1YPos
)

button2 = MyButton("button2", 400, 300, 10, 3, "wheat", "red", 1, True)
button2.setposFoo()
button2XPos, button2YPos = button2.xPos, button2.yPos 
button2 = Button(
    win,
    text                = button2.text,
    highlightbackground = button2.bg,
    fg                  = button2.fg,
    width               = button2.xDim,
    height              = button2.yDim,
    command             = button2.foo
)
button2.place(
    x = button2XPos,
    y = button2YPos
)

win.mainloop()
