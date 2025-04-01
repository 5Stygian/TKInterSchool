from tkinter import *

import random as r

win = Tk()

#xSize, xStartPos, ySize, yStartPos = 0, 0, 0, 0

class winSizeInit:
    def __init__(self, xSize, xStartPos, ySize, yStartPos):
        self.xSize     = xSize
        self.xStartPos = xStartPos
        self.ySize     = ySize
        self.yStartPos = yStartPos

    def winSizeInit(self, xSize, xStartPos, ySize, yStartPos):
        xSize     = r.randint(100,1000)
        xStartPos = r.randint(-700,700)

        ySize     = r.randint(100,1000)
        yStartPos = r.randint(-450,450)

        win.geometry(f"{xSize}x{ySize}+{xStartPos}+{yStartPos}")

        print(f"\n=========\nWidth = {xSize}\nHeight = {ySize}\nxPos = {xStartPos}\nyPos = {yStartPos}\n=========\n")

winSize = winSizeInit(0, 0, 0, 0)

win.config(bg="cornflower blue")
win.title("PyGame is a better lib")

def mainloop():
    winSize.winSizeInit()

# Widget Functions
def winResize():
    winSizeInit()
    win.geometry(f"{winSize.xSize}x{winSize.ySize}+{winSize.xStartPos}+{winSize.yStartPos}")

# Widgets
winResize = Button(
                win,
                text                = "Resize the window",
                highlightbackground = "white",
                fg                  = "red",
                width               = 5,
                height              = 5,
                command             = winResize)

winResize.place(
                x = winSize.xSize/2,
                y = winSize.ySize/2)

mainloop()
win.mainloop()
