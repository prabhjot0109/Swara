from tkinter import *
from tkinter import ttk, filedialog
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
# Canvas For imposing matplotlib graph with tkinter gui.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  
import os
import Swara_Backend

#Function for clearing Win
def clearWin(window):
      for widgets in window.winfo_children():
          widgets.destroy()

#-------------------- Login Win -------------------- #
def loginWin():
    clearWin(win_root)

    win_root.geometry("260x200")

    #Login Win Header Frame
    login_h_fr=Frame(win_root, bg="paleturquoise" )
    login_h_fr.pack(side=TOP, fill = X)

    #Login Label
    login_text=Label(login_h_fr, text="LOGIN" ,bg="paleturquoise", fg = "red", font= ("Posterama  20 bold"), padx = 200)
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


#---------------- File Input Win -------------------#

def fileWin():
        global user_file_loc
        global orgMusic_file_loc
        clearWin(win_root)

        #Fetching user and password for verification
        pswd = passvalue.get()
        user = uservalue.get()

        win_root.geometry("550x270")

        #File Header Frame
        file_h_fr=Frame(win_root, bg ="paleturquoise" )
        file_h_fr.pack(side=TOP, fill = X)

        #Header Text
        file_h_text=Label(file_h_fr, text="File Input" ,bg="paleturquoise", fg = "red", font= ("Posterama  20 bold"), padx = 200)
        file_h_text.pack()

        #Instruction Text
        inst_l = Label(win_root,text="Input your recorded music file and Original Music File Here.",
                        bg="paleturquoise" , fg = "Red", font = ("Posterama  10 bold") )
        inst_l.place(x = 30,y = 50)

        #  Function for taking File Input 
        def fileInput(b_x,b_y):
                file = filedialog.askopenfile(mode='r', filetypes=[('Music Files', '*.wav')])
                
                if file:
                        filePath = os.path.abspath(file.name)
                        path = filePath
                        file_loc_l = Label(win_root, text=str(filePath),font = "raleway 10 bold", bg="paleturquoise")
                        file_loc_l.place(x = b_x, y = (b_y + 30))                        
                        return path

        # #User File
        user_file_l = Label(win_root , text= "Your Music File :   " , bg="paleturquoise")
        user_file_l.place(x= 30 , y = 85)
        user_file_loc = fileInput(120,85)
        user_file_but = Button(win_root , text= "Browse",command=lambda : fileInput(120,85))
        user_file_but.place(x=120, y = 85)

        #Original File
        org_music_l = Label(win_root , text= "Original File : " , bg="paleturquoise")  
        org_music_l.place(x = 30,y=140)
        orgMusic_file_loc = fileInput(120,140)
        org_file_but = Button(win_root , text= "Browse",command=lambda : fileInput(120,140))
        org_file_but.place(x=120, y = 140)

        
        # Plot and Compare button
        plot_and_compare_button = tk.Button(win_root, text="Plot and Compare",
        command=graphWin)

        plot_and_compare_button.place(x=180, y = 220)
        

#---------------- Graph Input Win -------------------#
def graphWin():
        global user_file_loc
        global orgMusic_file_loc              
        clearWin(win_root)
        win_root.geometry("1400x700") 
        win_root.configure(bg="paleturquoise")
        win_root.title("Graph Input")

        #Graph Window Header Frame

        grp_h_fr=Frame(win_root, bg="paleturquoise" )
        grp_h_fr.pack(side=TOP, fill = X)

        # Label for graph Window
         
        grp_text=Label(grp_h_fr, text="GRAPH" , bg="paleturquoise" , fg = "red", font= ("Posterama  40"))
        grp_text.pack()
        
        result_text = tk.Label(win_root, text="" , bg="paleturquoise" ,fg = "green",  font= ("Posterama  20"))
        result_text.pack()               


        # Creating the graph holding frame

        grpframe = tk.Frame(win_root , bg ="paleturquoise")
        grpframe.pack(side=tk.LEFT)
        
        #Code execution and selection.

        try:    
                fig = Swara_Backend.plot_audio_files(user_file_loc,orgMusic_file_loc) 
                Swara_Backend.similarity_and_pitch(result_text,user_file_loc,orgMusic_file_loc)

        except:
                fig = Swara_Backend.plot_audio_files(user_file_loc,orgMusic_file_loc) 


        canvas = FigureCanvasTkAgg( fig, master=grpframe)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=2)
               
        # Creating close button    
        log_b = Button(win_root, fg="red", text = "CLOSE"  ,font = "raleway 12 bold", command = ackWin)
        log_b.place(x=680, y=660)

def ackWin():
                clearWin(win_root)
                win_root.geometry("400x300")
                win_root.title("Acknowledgement")

                # Graph Window Header Frame

                ack_h_fr = Frame(win_root, bg="paleturquoise")
                ack_h_fr.pack( fill=X)
                

                # Label for Acknowledgement Window
                
                ack_text = Label(ack_h_fr, text="""Thank You!!!""" , bg="paleturquoise", fg="red", font=("Posterama  20") , pady =60)
                ack_text.pack()
                
# --------------- Main Window --------------------- #

#Window Properties
win_root = Tk() 
win_root.geometry("450x440")
win_root.configure(bg="paleturquoise")
win_root.resizable(False,False)
win_root.title("Swara")

#Global Variables
user_file_loc = ""
orgMusic_file_loc = ""

uservalue = StringVar()
passvalue = StringVar()

#Welcome Text frame
wel_fr=Frame(win_root, bg="paleturquoise" )
wel_fr.pack(side=TOP, fill = X)

#Welcome Label
wel_text=Label(wel_fr, bg = "paleturquoise" , text="SWARA", fg = "red", font= ("Posterama  40 bold"), padx = 200)
wel_text.pack()

#Import image
sw_photo = PhotoImage(file="Images\logo.png")
sw_image = Label(image=sw_photo,bg = "paleturquoise")
sw_image.place(x = 230,y = 200,anchor="center")


#Start Button
start_b = Button(win_root, text = "START",font = " arial 20 bold", width = 10, height= 2, bd = 5 
                  ,fg="red" , command =  loginWin)
start_b.place(x = 230,y = 380,anchor='center')


win_root.mainloop()
