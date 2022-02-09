import tkinter

from tkinter import * #this means from tkinter you import everything

win = Tk() # this is for creating a variable win for the window

def nothing(): #This is for telling the menu what to do when clicked
    file = Toplevel(win)
    button = Button(file,text='do nothing')
    button.pack()
    
menubar = Menu(win)

filemenu = Menu(menubar) #This is for making the menu
filemenu.add_command(label='New Window', command=nothing)
filemenu.add_command(label='New File', command=nothing)
filemenu.add_command(label='Open', command=nothing)
filemenu.add_command(label='Close', command=nothing)
filemenu.add_separator() #This is for adding a separator line between th
filemenu.add_command(label='Save', command=nothing)
filemenu.add_command(label='Save as', command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Pugger', command=nothing)
filemenu.add_command(label='Close Tap', command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=win.quit)

menubar.add_cascade(label='File', menu=filemenu) #cascade is for adding the file menu into the parent menu

editmenu = Menu(menubar)
editmenu.add_command(label='undo', command=nothing)
editmenu.add_command(label='redo', command=nothing)
editmenu.add_separator()
editmenu.add_command(label='cut', command=nothing)
editmenu.add_command(label='copy', command=nothing)
editmenu.add_separator()
editmenu.add_command(label='paste', command=nothing)
editmenu.add_command(label='Select All', command=nothing)
editmenu.add_separator()
editmenu.add_command(label='Exit', command=win.quit)

menubar.add_cascade(label='Edit', menu=editmenu)

win.config(menu=menubar)
win.mainloop()