from tkinter import *
import random as r

win = Tk()
win.config(bg="cornflower blue")
win.title("PyGame is a better lib")

# Function to set the window size and position
def winSizeSet():
    xSize     = r.randint(100, 1000)
    ySize     = r.randint(100, 1000)
    xStartPos = r.randint(0, 700)
    yStartPos = r.randint(0, 450)
    
    win.geometry(f"{xSize}x{ySize}+{xStartPos}+{yStartPos}")
    print(f"\n=========\nWidth = {xSize}\nHeight = {ySize}\nxPos = {xStartPos}\nyPos = {yStartPos}\n=========\n")
    return xSize, ySize

# Function to resize the window
def winResize():
    winSizeSet()
    winResizeButton.place(
    x = xSize / 2 - 50,  # Adjusted for button width
    y = ySize / 2 - 20   # Adjusted for button height
    )

# Set the initial window size
xSize, ySize = winSizeSet()

# Create the resize button
winResizeButton = Button(
    win,
    text                = "Resize the window",
    highlightbackground = "white",
    fg                  = "red",
    width               = 20,
    height              = 2,
    command             = winResize
)

# Place the button in the center of the window
winResizeButton.place(
    x = xSize / 2 - 50,  # Adjusted for button width
    y = ySize / 2 - 20   # Adjusted for button height
)

# Start the main loop
win.mainloop()
