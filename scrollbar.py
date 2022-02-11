import tkinter

from tkinter import * #this means from tkinter you import everything

win = Tk() # this is for creating a variable win for the window

scrollbar = Scrollbar (win)
scrollbar.pack(side=RIGHT,fill=Y)

list = Listbox(win, yscrollcommand=scrollbar.set)

for line in range(100):
    list.insert(END, 'This is line no is ' + str(line))
    
list.pack(side=LEFT, fill=BOTH)
win.mainloop()