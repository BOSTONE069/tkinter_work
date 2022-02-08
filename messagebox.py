import tkinter

from tkinter import * #this means from tkinter you import everything
from tkinter import messagebox

win = Tk() # this is for creating a variable win for the window

def hello(): #this is for defining the information that thast the user is shown when he or she clicks the button
    messagebox.showinfo('from computer','Hello World')

b = Button(win, text='popup',command=hello)
b.pack()

win.mainloop()