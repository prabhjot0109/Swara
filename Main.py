from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import os

#import matplotlib.pyplot as plt


#Function for clearing Win
def clearWin(window):
      for widgets in window.winfo_children():
          widgets.destroy()

#---------------- File Input Win -------------------
def fileWin():
        clearWin(win_root)
        #Fetching user and password for verification
        pswd = passvalue.get()
        user = uservalue.get()

        win_root.geometry("400x270")

        #File Header Frame
        file_h_fr=Frame(win_root, borderwidth= 6, relief = GROOVE )
        file_h_fr.pack(side=TOP, fill = X)

        #Header Text
        file_h_text=Label(file_h_fr, text="File Input" ,bg="white", fg = "red", font= ("Posterama  20 bold"), padx = 200)
        file_h_text.pack()

        #Instruction Text
        inst_l = Label(win_root,text="Input your file and Original Music File Here.",
                        bg="paleturquoise" , fg = "Red", font = ("Posterama  10 bold") )
        inst_l.place(x = 10,y = 50)

        #Function for taking File Input 
        def fileInput(b_x,b_y):
                global filePath
                file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.py')])
                if file:
                        filePath = os.path.abspath(file.name)
                        file_loc_l = Label(win_root, text=str(filePath),font = "raleway 10 bold", bg="paleturquoise")
                        file_loc_l.place(x = b_x, y = (b_y + 30))
                        filePath = str(filePath)
                        

        #User File
        user_file_l = Label(win_root , text= "Your File :   " , bg="paleturquoise")
        user_file_l.place(x= 30 , y = 85)
        user_file_but = Button(win_root , text= "Browse",command=lambda : fileInput(120,85))
        user_file_but.place(x=120, y = 85)
        user_file_loc = filePath
        
 

        #Original File
        org_music_l = Label(win_root , text= "Original : " , bg="paleturquoise")  
        org_music_l.place(x = 30,y=140)
        org_file_but = Button(win_root , text= "Browse",command=lambda : fileInput(120,140))
        org_file_but.place(x=120, y = 140)
        orgMusic_file_loc = filePath

        
        
        #Process Button
        process_b = Button(win_root, fg="red", text = "Process"  ,font = "raleway 12 bold")
        process_b.place(x = 110, y = 210)

        print(user_file_loc,orgMusic_file_loc,sep="\n")
        


#---------------- Graph Input Win -------------------
def graphWin():
                          
        clearWin(win_root)
        win_root.geometry("600x600") 
        win_root.configure(bg="paleturquoise")
        win_root.title("Graph Input")

        #Graph Window Header Frame

        grp_h_fr=Frame(win_root, bg="paleturquoise", borderwidth= 6, relief = "sunken" )
        grp_h_fr.pack(side=TOP, fill = X)

        # Label for graph Window

        grp_text=Label(grp_h_fr, text="GRAPH" ,bg="white", fg = "red", font= ("Posterama  20 bold"), padx = 200)
        grp_text.pack()


        # Creting the graph importing label
        result = Label(win_root, text='', bg='white', width=80 ,font= ("Posterama  20 bold"))     
        result.place(x=150, y=160 , height =400)
        # Creating the graph
        #graph_img = ImageTk.PhotoImage(Image.open("graph.png"))
        #plt.plot(df['Frequency'],df['Pitch'],marker ='o',color = 'green')
        plt.xticks(rotation="vertical")
        plt.xlabel("Frequency")
        plt.ylabel("NOPitch")
        plt.legend(["CuFrequency"])
        plt.show()







        # Creating close button
    
        log_b = Button(win_root, fg="red", text = "CLOSE"  ,font = "raleway 12 bold", command = ackWin)
        log_b.place(x =170, y=180)

        

#-------------------- Login Win --------------------
def loginWin():
    clearWin(win_root)

    win_root.geometry("260x200")

    #Login Win Header Frame
    login_h_fr=Frame(win_root, bg="paleturquoise", borderwidth= 6, relief = GROOVE )
    login_h_fr.pack(side=TOP, fill = X)

    #Login Label
    login_text=Label(login_h_fr, text="LOGIN" ,bg="white", fg = "red", font= ("Posterama  20 bold"), padx = 200)
    login_text.pack()
    

    #User
    user = Label(win_root , text= "Username ID  :   ", bg="paleturquoise")
    user.place(x= 30 , y = 58)

    userentry = Entry(win_root , textvariable =uservalue )
    userentry.place(x=120, y = 58)

    #Password
    password = Label(win_root , text= "Password : ", bg="paleturquoise")  
    password.place(x = 30,y=80)

    passentry = Entry(win_root , textvariable = passvalue)
    passentry.place(x=120 ,y = 80)
    
    #Login Button
    log_b = Button(win_root, fg="red", text = "Login"  ,font = "raleway 12 bold", command = fileWin)
    log_b.place(x = 170, y = 130)

    #Create User Button
    c_user_b = Button(win_root, fg = "red", text = "Sign - Up", font = " raleway 12 bold" )
    c_user_b.place(x = 30, y = 130)



#__main__
#--------------- Main Window ---------------------
#Window Properties
win_root = Tk() 
win_root.geometry("450x460")
win_root.configure(bg="paleturquoise")
win_root.resizable(False,False)
win_root.title("Swara")

#Global Variables
filePath = ""
uservalue = StringVar()
passvalue = StringVar()

#Welcome Text frame
wel_fr=Frame(win_root, bg="white", borderwidth= 6, relief = GROOVE )
wel_fr.pack(side=TOP, fill = X)

#Welcome Label
wel_text=Label(wel_fr, text="SWARA", fg = "red", font= ("Posterama  40 bold"), padx = 200)
wel_text.pack()

#Import image
sw_photo = PhotoImage(file="Images/logo.png")
sw_image = Label(image=sw_photo)
sw_image.place(x = 230,y = 200,anchor="center")

#Start Button
start_b = Button(win_root, text = "START",font = " arial 20 bold", width = 10, height= 2, bd = 5 
                  ,fg="red" , command =  loginWin)
start_b.place(x = 230,y = 380,anchor='center')


win_root.mainloop()