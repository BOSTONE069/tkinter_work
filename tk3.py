import tkinter

from tkinter import *  #this means from tkinter you import everything

win = Tk() # this is for creating a variable win for the window
def pr(): # this is the command to be printed when the button is clicked 
    print("Hello, World") 
win.geometry("700x400") #this is for controlling the height and width of the application

b = Button(win, text="button", command=pr, padx=20 , pady=20 , activeforeground="red") #this is for adding a button into the window
b.place(x=100, y=200) #the place function helps in controlling the position of the button

b2 = Button(win, text='bu') #this is for creating another button
b2.place(x=300, y=280) #the place function helps in controlling the position of the button

win.mainloop()