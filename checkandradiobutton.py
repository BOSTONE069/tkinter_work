import tkinter

from tkinter import *  # this means from tkinter you import everything

win = Tk()  # this is for creating a variable win for the window
c1 = IntVar() # this is a initialized variable to be used in the buttons
c2 = IntVar()
#this is for creating check buttons in the windows area
cb = Checkbutton(win, text='Music', offvalue=0, onvalue=1, height=5, width=10, variable=c1) 
cb.pack()
cb2 = Checkbutton(win, text='Laundry', offvalue=0, onvalue=1, height=5, width=10, variable=c2)
cb2.pack()

#this is for creating radio button
var = IntVar()
r1 = Radiobutton(win, text='Option 1', variable=var, value=1)
r1.pack()
r2 = Radiobutton(win, text='Option 2', variable=var, value=2)
r2.pack()
r3 = Radiobutton(win, text='Option 3', variable=var, value=3)
r3.pack()


win.mainloop()
