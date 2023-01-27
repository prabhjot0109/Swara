# Importing the modules
from tkinter import *
import tkinter as tk
import tkinter.font as font
win = Tk()


# Creating the window
win.geometry('500x460') # Changes Size of win
win.resizable(False,False) # It is used to fix a size for a win
win.title('SWARA')# Gives the title to window
win.configure(bg='paleturquoise') # It configures features of window once it is made

text1 = Label(win,text="Test",font = ("Times",24),bg = 'paleturquoise') #Label
text1.place(relx = 1, rely = 2)

fr = Frame(win,bd = 10,width  = 400, height = 200)
#fr.grid(row = 1,column = 1)


# Creating the fonts
font1 = font.Font(family='Daytona Condensed Light  ', size='30')
font2 = font.Font(family='times', size='18')
font3 = font.Font(family='arial', size='16')


# Creating the swara label
main = tk.Label(win, text='SWARA',font = font1, fg='blue' , bg= 'paleturquoise')
main['font'] = font1
main.place(x=250 , y= 30, anchor='center')


# Creating the art label
art = tk.Label(win, text='Python Program', fg='crimson' , bg= 'paleturquoise')
art['font'] = font2
art.place(x=170, y=420)
win.mainloop()

