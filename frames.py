import tkinter

from tkinter import * #this means from tkinter you import everything

win = Tk() # this is for creating a variable win for the window
frame = Frame(win) #this is for making frame one
frame.pack()

frame2 = Frame(win)#this is for making frame 2
frame2.pack(side=BOTTOM)

rb = Button(frame, text='Red', fg='red') #This includes a button in the first frame
rb.pack(side=LEFT)

gb = Button(frame2, text='Green', fg='Green') #This includes a button in the second frame
gb.pack(side=BOTTOM)

win.mainloop()