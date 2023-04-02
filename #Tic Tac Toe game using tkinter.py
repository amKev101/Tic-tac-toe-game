#Tic Tac Toe game using tkinter

#Importing modules
from tkinter import *
import tkinter.messagebox

#Window defined
root = Tk()

root.iconbitmap('tic-tac-toe.ico')

root.title('Tic-Tac-Toe')

root.resizable(False,False)

click = True

#Count variable to check the no. of turns
count = 0

btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

xPhoto = PhotoImage(file = 'cross.png')
oPhoto = PhotoImage(file = 'happy.png')

#Grid buttons
def start():
    button1 = Button(root,height=9,width=19,bd=.5,relief = 'sunken',bg = '#ccfff7',textvariable = btn1,
                     command=lambda: press(1,0,0)) 
    button1.grid(row=0,column=0)

    button2 = Button(root,height=9,width=19,bd = .5,relief = 'sunken',bg = '#ccfff7',textvariable = btn2,
                     command=lambda: press(2,0,1))
    button2.grid(row=0,column=1)

    button3 = Button(root,height=9,width=19,bd = .5,relief = 'sunken',bg = '#ccfff7',textvariable = btn3,
                     command=lambda: press(3,0,2))
    button3.grid(row=0,column=2)