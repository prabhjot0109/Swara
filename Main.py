from tkinter import *

#Function for clearing Win
def clearWin(window):
      for widgets in window.winfo_children():
          widgets.destroy()

#---------------- File Input Win -------------------
def fileWin():
        clearWin(win_root)
        pswd = passvalue.get()
        user = uservalue.get()
        

#-------------------- Login Win --------------------
def loginWin():
    clearWin(win_root)

    #User
    user = Label(win_root , text= "Username ID -  ")
    user.place(x=50,y=50)

    userentry = Entry(win_root , textvariable =uservalue )
    userentry.place(x=23, y = 28)

    #Password
    password = Label(win_root , text= "Password - ")   
    password.place(x=70,y =70)

    passentry = Entry(win_root , textvariable =passvalue )
    passentry.place(x=10,y=20)
    
    #Start Button
    log_win = Button(win_root, fg="red", text = "START"  ,font = " arial 10 bold", bg= "white", command = fileWin)
    log_win.pack(side = BOTTOM , padx = 20 , anchor = SE) 

#__main__

#Global Variables
uservalue = StringVar()
passvalue = StringVar()

#--------------- Main Window ---------------------
win_root = Tk() 

#Geometry Of Win
win_root.geometry("500x600")
win_root.resizable(False,False)

#Window Title
win_root.title("Swara")

#Frame in Tkinter
wel_fr=Frame(win_root, bg="white", borderwidth= 6, relief = SUNKEN )
wel_fr.pack(side=TOP, fill = X)

#Welcome Label
wel_text=Label(wel_fr, text="""Welcome to Swara\nA way to trace your progress""" ,
                 bg="white", fg = "red", font= "times 20 bold", padx = 200)
wel_text.pack()

#Import image
sw_photo = PhotoImage(file="Images/logo.png")
sw_image = Label(image=sw_photo)
sw_image.pack(side = TOP, fill = X , padx=34 , pady =56)

#Swara Text
sw_label=Label(text="SWARA", bg="green" , fg="blue", padx= 11,pady = 23,font= ("arial",23, "bold")
            ,borderwidth= 5, relief= SUNKEN)
sw_label.pack()

#Start Button
start_b = Button(win_root, fg="red", text = "START"  ,font = " arial 10 bold", bg= "white" , command =  loginWin)
start_b.pack(side = BOTTOM)

win_root.mainloop()