from tkinter import *

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
        else:
            pass

    def foo(self):
        if self.correct == True:
            win.config(bg="black")
        elif self.correct == False:
            win.config(bg="white")
        else:
            pass

myButton1 = MyButton("button1", 400, 300, 10, 3, "wheat", "red", 0, False)
myButton1.setposFoo()

button1 = Button(
    win,
    text                = myButton1.text,
    highlightbackground = myButton1.bg,
    fg                  = myButton1.fg,
    width               = myButton1.xDim,
    height              = myButton1.yDim,
    command             = myButton1.foo
)
button1.place(
    x = myButton1.xPos,
    y = myButton1.yPos
)

myButton2 = MyButton("button2", 400, 300, 10, 3, "wheat", "red", 1, True)
myButton2.setposFoo()

button2 = Button(
    win,
    text                = myButton2.text,
    highlightbackground = myButton2.bg,
    fg                  = myButton2.fg,
    width               = myButton2.xDim,
    height              = myButton2.yDim,
    command             = myButton2.foo
)
button2.place(
    x = myButton2.xPos,
    y = myButton2.yPos
)

win.mainloop()
