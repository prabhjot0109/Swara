from tkinter import *

root = Tk()

#width x height
root.geometry("500x400")
#Windoe title
root.title("Swara")
#width,height
root.minsize(200,100)
#width,height
root.maxsize(800,900)


# Frame in tkinter
f1=Frame(root, bg="white", borderwidth= 2, relief = SUNKEN )
f1.pack(side=LEFT, fill = Y)

f2=Frame(root, bg="white", borderwidth= 6, relief = SUNKEN )
f2.pack(side=TOP, fill = X)

l=Label(f1, text="Python Project" ,bg="red")
l.pack(pady=142)

l=Label(f2, text="""Welcome to Swara.
                    A way to trace your progress """ ,bg="white", fg = "red",
                     font= "times 20 bold", padx = 200)
l.pack()

# work of command
def win():
    
    win_root = Tk()
    win_root.geometry("500x400")
    user=Label(win_root , text= "Username ID -  ")
    password=Label(win_root , text= "Password - ")
    


    user.place(x=45,y=54)
    password.place(x=54,y =0)

    #Variable classes in tkinter
    #BooleanVar, DoubleVar, IntVar, StringVar.

    uservalue= StringVar()
    passvalue= StringVar()

    userentry = Entry(win_root , textvariable =uservalue )
    passentry = Entry(win_root , textvariable =passvalue )

    userentry.place(x=23, y = 28)
    passentry.place(x=10,y=20)
    # c1 = Button(, fg="red", text = "Submit"  ,font = " arial 10 bold", bg= "white" 

    #        , command = opt)
    # c1.pack(side = BOTTOM , padx = 20 , anchor = SE)
    def opt():


        opt_root = Tk()
        opt_root.geometry("500x400")
        
        print(uservalue.get())
        print(passvalue.get())

        opt_root.mainloop()
    b1=Frame(win_root, bg="white", borderwidth= 6 , relief= SUNKEN)
    b1.pack(side=BOTTOM)

    c1 = Button(b1, fg="red", text = "START"  ,font = " arial 10 bold", bg= "white" 

     , command = opt)
    c1.pack(side = BOTTOM , padx = 20 , anchor = SE) 
    # Button(text = "Submit",command=opt).place(row=2, column=2)
   

    

    win_root.mainloop()
   

f3=Frame(root, bg="white", borderwidth= 6 , relief= SUNKEN)
f3.pack(side=BOTTOM)

b1 = Button(f3, fg="red", text = "START"  ,font = " arial 10 bold", bg= "white" 

, command = win)
b1.pack(side = BOTTOM , padx = 20 , anchor = SE)



#Import image
photo = PhotoImage(file="Images/logo.png")
image = Label(image=photo)

#Pack attributes
# anchor = "Write direction in which text or image is to be alligned"
# example- anchor = "ne"
# example- anchor = "sw"
# side = TOP , BOTTOM, LEFT, RIGHT
# fill= X #filles in x axis
# fill= Y #filles in y axis
# 
# padx
# pady

image.pack(side = TOP, fill = X , padx=34 , pady =56)


# Label
# Important label options
# text =adds the text
# bd =background
# fg =foreground
# font =sets the font
# 2 ways-
# 1)font= "arial 23 bold "
# 2)font= ("arial",23, "bold"))
#borderwidth = defines border width
# padx= padding in x
# pady= padding in y
# relief = SUNKEN, RAISED, GROOVE , RIDGE [Types pf border]
# Used for border styling 

label=Label(text="SWARA", bg="green" , fg="blue", padx= 11,pady = 23,font= ("arial",23, "bold")# 1)font= "arial 23 bold "
,borderwidth= 5, relief= SUNKEN)

label.pack()


root.mainloop()