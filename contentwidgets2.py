import tkinter

from tkinter import *  # this means from tkinter you import everything

win = Tk()  # this is for creating a variable win for the window
l1 = Label(win,text='First no')
l1.grid(row=1,column=0)
l2 = Label(win, text='Second no')
l2.grid(row=2, column=0)
label = Label(win)
label.grid(row=6,column=2)

x1 = StringVar()#this is defining the variables to be entered into the box
x2 = StringVar()  # this is defining the variables to be entered into the box

e1 = Entry(win,textvariable=x1) #this is for making the entry box 
e1.grid(row=1,column=2) # this is for defining the position of the entry box
e2 = Entry(win, textvariable=x2)  # this is for making the entry box
e2.grid(row=2, column=2) #this is for defining the position of the entry box

win.mainloop()
