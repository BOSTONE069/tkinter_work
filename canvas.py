import tkinter

from tkinter import *  # this means from tkinter you import everything

win = Tk()  # this is for creating a variable win for the window

c = Canvas(win, height=400 , width=600, bg='blue') #this defines the outlook of the canvas
coord = 10,50,240,210
arc = c.create_arc(coord,start=0, extent=150, fill='red') #this defines the arc that is being created within the canvas from the coordinates

c.pack()

win.mainloop()
