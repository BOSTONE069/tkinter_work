import tkinter

from tkinter import * #this means from tkinter you import everything

win = Tk() # this is for creating a variable win for the window
#thi is to enable the crweation of a window on top of the other
win.title('first') #this is for creating first window
top = Toplevel()
top.title('second') #this is for creating second window

win.mainloop()