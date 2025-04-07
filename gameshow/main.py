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

test = MyButton("test", 450, 350, 10, 3, "wheat", "red", 0, False)
test.setposFoo()
testXPos, testYPos = test.xPos, test.yPos
test = Button(
    win,
    text                = test.text,
    highlightbackground = test.bg,
    fg                  = test.fg,
    width               = test.xDim,
    height              = test.yDim,
    command             = test.foo
)
test.place(
    x = testXPos,
    y = testYPos
)

test2 = MyButton("test2", 450, 350, 10, 3, "wheat", "red", 1, True)
test2.setposFoo()
test2XPos, test2YPos = test2.xPos, test2.yPos 
test2 = Button(
    win,
    text                = test2.text,
    highlightbackground = test2.bg,
    fg                  = test2.fg,
    width               = test2.xDim,
    height              = test2.yDim,
    command             = test2.foo
)
test2.place(
    x = test2XPos,
    y = test2YPos
)

win.mainloop()
