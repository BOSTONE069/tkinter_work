import tkinter

from tkinter import * #this means from tkinter you import everything

win = Tk() # this is for creating a variable win for the window
win.geometry("700x400") #this is for controlling the height and width of the application

b = Button(win, text="button") #this is for adding a button into the window
b.grid(row=2, column=1) #the grid function helps in controlling the position of the button

b2 = Button(win, text='bu') #this is for creating another button
b2.grid(row=1, column=1) #the grid function helps in controlling the position of the button

win.mainloop()