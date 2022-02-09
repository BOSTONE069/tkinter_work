import tkinter

from tkinter import * #this means from tkinter you import everything

win = Tk() # this is for creating a variable win for the window

#creating menu button
mb = Menubutton(win,text='File')
mb.grid()
mb.menu = Menu(mb)
mb['menu'] = mb.menu
 
#this are declared variables for the menu
x1 = IntVar()
x2 = IntVar()

#This is adding menu to the menu button when clicked using the variables
mb.menu.add_checkbutton(label='open',variable=x1)
mb.menu.add_checkbutton(label='close',variable=x2)

mb.pack()

win.mainloop()