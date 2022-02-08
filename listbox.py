import tkinter

from tkinter import * #this means from tkinter you import everything

win = Tk() # this is for creating a variable win for the window

lb = Listbox(win) #thi is for initalizzing the listbox
lb.insert(1,'python') #this is for inserting values in the list box
lb.insert(2,'c')
lb.insert(3,'c++')
lb.insert(4,'jquery')
lb.insert(5,'ruby')

lb.pack()

win.mainloop()