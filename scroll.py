import tkinter

from tkinter import * #this means from tkinter you import everything

win = Tk() # this is for creating a variable win for the window

s = Scale(win) #This is fo defining a scale in the scroll bar
s.pack()

sb = Spinbox(win, from_= 0 , to=10)
sb.pack()



win.mainloop()