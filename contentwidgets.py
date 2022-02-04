import tkinter

from tkinter import *  # this means from tkinter you import everything

win = Tk()  # this is for creating a variable win for the window
l = Label(win, text='username') #This shows a label
l.pack(side=LEFT) #this includes the position of the label
e = Entry(win) #thios shows the entry box foor text
e.pack(side=RIGHT)


win.mainloop()
