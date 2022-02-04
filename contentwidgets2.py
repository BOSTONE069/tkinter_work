import tkinter

from tkinter import *  # this means from tkinter you import everything
from functools import partial

win = Tk()  # this is for creating a variable win for the window

def sum(label,x1,x2): # this defines the sun fuctiona at the button
    n1 = (x1.get()) #this Variable gets entry from the text box
    n2 = (x2.get())  # this Variable gets entry from the text box
    sum = int(n1) + int(n2)
    label.config(text='sum is : %d' %sum)
    return

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

sum = partial(sum,label,x1,x2)
button = Button(win, text="calculate", command=sum) #this is a button for calculation
button.grid(row=3,column=0)

win.mainloop()
