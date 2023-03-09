# Libraries for creating GUI
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkcalendar import *

# Canvas For imposing matplotlib graph and toolbar with tkinter gui.
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg , NavigationToolbar2Tk 

# Libraries for recording voice and processing
import pyaudio
import wave
import os

# Importing Custom Files
import Swara_Backend
import Swara_Database


#Function for clearing Win
def clearWin(window):
      for widgets in window.winfo_children():
          widgets.destroy()

#Function for taking File Input 
def fileInput(win,b_x,b_y):
        file = filedialog.askopenfile(mode='r', filetypes=[('Music Files', '*.wav')])
        
        if file:
                filePath = os.path.abspath(file.name)
                path = filePath
                file_loc_l = Label(win , text = filePath ,font = "raleway 10 bold", bg="paleturquoise")
                file_loc_l.place(x = b_x, y = (b_y + 30))                        
                return path

#Function for recordign Audio
def recording(win,sec_e):
        sec = sec_e.get()
        FRAMES_PER_BUFFER = 3200
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000

        # Calling Python library to record audio
        audio = pyaudio.PyAudio()

        record = audio.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=FRAMES_PER_BUFFER
        )
        
        # Creates a label when recording completes.
        ch2 = Label(win , text= "Your voice is Recorded!" , bg="paleturquoise" ,font= ("Posterama  16 bold"))
        ch2.place(x= 140 , y = 220)

        # Defines recording interval by taking input from user.
        seconds = float(sec)
        frames = []
        second_tracking = 0
        second_count = 0
        for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
                ch3 = Label(win, textvariable = f'Time Left: {seconds - second_count} seconds' , bg="paleturquoise")
                ch3.place(x= 30 , y = 130)
                data = record.read(FRAMES_PER_BUFFER)
                frames.append(data)
                second_tracking += 1
                second_count += 1


        record.stop_stream()
        record.close()
        audio.terminate()

        # Stores recorded audio file
        specimen = wave.open('Audio/user.wav', 'wb')
        specimen.setnchannels(CHANNELS)
        specimen.setsampwidth(audio.get_sample_size(FORMAT))
        specimen.setframerate(RATE)
        specimen.writeframes(b''.join(frames))
        specimen.close()

#-------------------- Login Win -------------------- #

def loginWin():
        clearWin(win_root)

        win_root.geometry("260x200")

        #Login Win Header Frame
        login_h_fr=Frame(win_root, bg="paleturquoise" )
        login_h_fr.pack(side=TOP, fill = X)

        #Login Label
        login_text=Label(login_h_fr, text="LOGIN" ,bg="paleturquoise", fg = "red", font= ("Posterama  20 bold"), padx = 200 , pady = 10)
        login_text.pack()

        #User
        user = Label(win_root , text= "Username ID  :   ", bg="paleturquoise")
        user.place(x= 30 , y = 58)

        userEntry = Entry(win_root , textvariable =uservalue )
        userEntry.place(x=120, y = 58)

        #Password
        password = Label(win_root , text= "Password : ", bg="paleturquoise")  
        password.place(x = 30,y=80)

        passEntry = Entry(win_root , textvariable = passvalue, show = "*")
        passEntry.place(x=120 ,y = 80)
        
        #Login Button
        database = Swara_Database.Database()
        login = lambda : database.login(userEntry,passEntry,chooseWin)  
        log_b = Button(win_root, fg="red", text = "Login"  ,font = "raleway 12 bold", command = login) #Checks and verify the login details
        log_b.place(x = 160, y = 130)

        #Create User Button
        c_user_b = Button(win_root, fg = "red", text = "Sign - Up", font = " raleway 12 bold" ,command= createUserWin)
        c_user_b.place(x = 30, y = 130)


#----------------------------Sign Up window----------------------#

def createUserWin():

    global signUp_win

    #Window Properties
    signUp_win = Toplevel(win_root)
    signUp_win.geometry("410x500")
    signUp_win.resizable(False,False)
    signUp_win.title("Sign - Up")    
    signUp_win.configure(bg="paleturquoise")  
    signUp_win.grab_set()


    #Heading Frame
    h_frame= Frame(signUp_win , bg="paleturquoise" ,bd=10)
    h_frame.grid(row=0,column=0)
    h= Label(h_frame ,text="Create Account",font=("Times 20 bold") , bg="paleturquoise")
    h.grid(padx=100,pady=2)

    #Details Frame
    details_frame= Frame(signUp_win , bg="paleturquoise")
    details_frame.grid(row=1,column=0)

    #Mobile No.
    mobile_no_l= Label(details_frame,text="Mobile Number : " , bg="paleturquoise")      
    mobile_no_l.grid(row=0,column=0,padx=5,pady=10)
    user_create_mobile.set("")
    
    mobile_no_e= Entry(details_frame,width=20,justify="center",textvariable=user_create_mobile)
    mobile_no_e.config(state="normal")
    mobile_no_e.grid(row=0,column=1)

    #E-mail
    email_l= Label(details_frame,text="Email Address : " , bg="paleturquoise")
    email_l.grid(row=1,column=0,padx=5,pady=10,sticky='w')
    user_create_email.set("")
    
    email_e= Entry(details_frame,width=20,justify="center",textvariable=user_create_email)
    email_e.config(state="normal")
    email_e.grid(row=1,column=1)

    #Function for Enabling Rest of the Entry boxes
    def enableEntry():
        first_name_e.config(state = "normal")
        last_name_e.config(state = "normal")
        username_e.config(state = "normal")
        password_e.config(state = "normal")
        choose.config(state = "normal")
        submit_b.config(state = "normal")
        check_b.destroy()

    #Check Button
    check_me = lambda : database.regCheck(mobile_no_e,email_e,enableEntry)
    check_b = Button(details_frame,text="Check", command = check_me , fg="red" ,  font= ("times  10 bold"))
    check_b.grid(row=1,column=2,padx=10)
    
    #Username
    username_l= Label(details_frame,text="Username : " , bg="paleturquoise")
    username_l.grid(row=2,column=0,padx=5,pady=10,sticky='w')
    user_create_username.set("")
    
    username_e= Entry(details_frame,width=20,justify="center",textvariable=user_create_username)
    username_e.grid(row=2,column=1)
    username_e.config(state="disabled")

    #Password
    password_l= Label(details_frame,text="Password : " , bg="paleturquoise")
    password_l.grid(row=3,column=0,padx=5,pady=10,sticky='w')
    user_create_password.set("")
    
    password_e= Entry(details_frame,width=20,justify="center",show = "*",textvariable=user_create_password)
    password_e.grid(row=3,column=1)
    password_e.config(state="disabled")

    #First Name
    first_name_l= Label(details_frame,text="First Name : " , bg="paleturquoise")
    first_name_l.grid(row=4,column=0,padx=5,pady=10,sticky='w')
    user_create_firstname.set("")
    
    first_name_e= Entry(details_frame,width=20,justify="center",textvariable=user_create_firstname)
    first_name_e.grid(row=4,column=1)
    first_name_e.config(state="disabled")

    #Last Name
    last_name_l= Label(details_frame,text="Last Name : " , bg="paleturquoise")
    last_name_l.grid(row=5,column=0,padx=5,pady=10,sticky='w')
    user_create_lastname.set("")
    
    last_name_e= Entry(details_frame,width=20,justify="center",textvariable=user_create_lastname)
    last_name_e.grid(row=5,column=1)
    last_name_e.config(state="disabled")

    #DOB
    dob_l= Label(details_frame,text="Date Of Birth : " , bg="paleturquoise")
    dob_l.grid(row=6,column=0,padx=5,pady=10,sticky='w',columnspan=2)
    
    date_l= Label(details_frame , bg="paleturquoise")
    date_l.grid(row=6,column=1,padx=5,pady=10)
    user_create_dob.set("")          

    #Function for Choosing Date
    def choose_date():
        date_picker= Toplevel(signUp_win)
        date_picker.resizable(False,False)
        date_picker.title("Date Picker")
        date_picker.grab_set()
        dob_e= Calendar(date_picker,selectmode='day',year=2000,month=1,day=1)                
        dob_e.pack()

        #Function for Saving chosen Date
        def picked():
            date_l.config(text=dob_e.get_date())
            user_create_dob.set(dob_e.get_date())                    
            date_picker.destroy()
        
        #Ok Button
        ok= Button(date_picker,text="OK",bd=5,command=picked , fg= "red")
        ok.pack(pady=10)           

    #Choose Button
    choose= Button(details_frame,text="Choose Date",command=choose_date, fg="red", font= ("times  10 bold"))
    choose.grid(row=6,column=2)
    choose.config(state="disabled")
    choose.config(state="disabled")

   
    #Sumbit Button
    submit = lambda : database.regSumbit(signUp_win, user_create_email, user_create_mobile,user_create_username,user_create_password,user_create_firstname,user_create_lastname,user_create_dob ) 
    submit_b =Button( signUp_win , text="SUBMIT",width=10,bd=6,font= ("Posterama  20 bold"), command = submit , fg = "red")
    submit_b.config(state="disabled")
    submit_b.place(x=100 , y=360)


    #Function for going back to Login Win
    def back():
        signUp_win.destroy()

    #Back Button
    back_b=Button(signUp_win ,text="<--- Go Back to Login",bd=6,command=back , fg = "black")
    back_b.place( x= 6 , y= 450 )
        

#-----------------Choose option window---------------#

def chooseWin():

        global cnd_root

        #Command Window Properties
        cnd_root = Toplevel(win_root)
        cnd_root.grab_set() 
        cnd_root.configure(bg="paleturquoise")
        cnd_root.resizable(False,False)
        cnd_root.title("Option Window")
        cnd_root.geometry("280x200")

        #Command Win Header Frame
        ch_h_fr=Frame(cnd_root, bg="paleturquoise" )
        ch_h_fr.pack(side=TOP, fill = X)

        #Command Label
        ch_text=Label(ch_h_fr, text="COMMAND" ,bg="paleturquoise", fg = "red", font= ("Posterama  20 bold"), padx = 200 , pady= 20)
        ch_text.pack()
        
        #Upload Button
        up_b = Button(cnd_root, fg = "red", text = "Upload File", font = " raleway 12 bold" , command = fileWin)
        up_b.place(x = 20, y = 90)

        #Record Button
        rec_b = Button(cnd_root, fg="red", text = "Record Audio"  ,font = "raleway 12 bold", command = recordWin )
        rec_b.place(x = 140, y = 90)

        #Function for going back to Login Window

        def back():
                cnd_root.destroy()

        #Back Button
        back_b=Button(cnd_root, text="<--- Go Back to Login",bd=6,command=back , fg = "black")
        back_b.place(x=6 , y=160 )  


#-----------------Record audio window---------------#

def recordWin():
    
    global rec_root

    #Record Win Configurations
    rec_root = Toplevel(cnd_root) 
    rec_root.grab_set()
    rec_root.geometry("520x450")
    rec_root.configure(bg="paleturquoise")
    rec_root.resizable(False,False)
    rec_root.title("Record Audio")

    # Defining files path variables

    global orgMusic_file_loc
    global user_file_loc

    user_file_loc = "Audio/user.wav"

    #Command Win Header Frame
    ch_h_fr=Frame(rec_root, bg="paleturquoise" )
    ch_h_fr.pack(side=TOP, fill = X)
        
    #Command Label
    ch_text=Label(ch_h_fr, text="Record Audio" ,bg="paleturquoise", fg = "red", font= ("Posterama  25 bold"), padx = 200 , pady= 10)
    ch_text.pack()

    # Original File upload label
    org_music_l = Label(rec_root , text= "Original File : " , bg="paleturquoise",  font= ("Posterama  12 bold"))
    org_music_l.place(x= 20 , y= 80)
    orgMusic_file_loc = fileInput(rec_root,20,80)
    org_file_but = Button(rec_root , text= "Browse",command=lambda : fileInput(rec_root,20 , 80))#(120,140))
    org_file_but.place(x= 165 , y= 80)
    
    #Interval input label
    interval_l = Label(rec_root , text= "Enter recording interval : \n(in Seconds)  " , bg="paleturquoise",  font= ("Posterama  12 bold"))
    interval_l.place(x= 35 , y= 150)

    # Interval input entry box
    sec_e = Entry(rec_root,font = "Posterama 15 bold", width = 10)
    sec_e.place(x= 260 , y= 150)
    

    # Record Audio button
    record_button = Button(rec_root, text="Record Audio", command= lambda : recording(rec_root,sec_e) , font = " arial 15 bold", width = 14, height= 2,
                relief = RAISED,fg="red" ) 
    record_button.place(x=170 , y=260)

    # Plot and compare button
    next_button = Button(rec_root, text ="Plot and Compare", command=graphWin ,font = " arial 15 bold", width = 16, height= 2
                ,fg="red" , relief = RAISED )
    next_button.place(x= 160 , y= 350)
    
    #Function for going back to Command Window
    def back():
        rec_root.destroy()
        
    #Back Button
    back_b=Button(rec_root ,text="<--- Go Back",bd=6,command=back , fg = "black")
    back_b.place(x= 10 , y=400)
  


#------------------ File Input Win -------------------#

def fileWin():

        global f_root

        #File Input Win Configuration        
        f_root = Toplevel(cnd_root)
        f_root.grab_set() 
        f_root.configure(bg="paleturquoise")
        f_root.resizable(False,False)
        f_root.title("File Input")
        f_root.geometry("500x270")
        
        # Defining file path variables

        global user_file_loc
        global orgMusic_file_loc
        
        #Global Variables
        user_file_loc = ""
        orgMusic_file_loc = ""

        #File Header Frame
        file_h_fr=Frame(f_root, bg ="paleturquoise" )
        file_h_fr.pack(side=TOP, fill = X)

        #Header Text
        file_h_text=Label(file_h_fr, text="File Input" ,bg="paleturquoise", fg = "red",
                          font= ("Posterama  20 bold"), padx = 200 , pady = 10)
        file_h_text.pack()

        #Instruction Text
        inst_l = Label(f_root,text="Input your recorded music file and Original Music File Here.",
                        bg="paleturquoise" , fg = "Red", font = ("Posterama  12 bold") )
        inst_l.place(x = 20,y = 50)

        #User File
        user_file_l = Label(f_root , text= "Recorded File :   " , bg="paleturquoise",  font= ("times  12  bold"))
        user_file_l.place(x= 30 , y = 85)
        user_file_but = Button(f_root , text= "Browse",command=lambda : fileInput(f_root,30,85))
        user_file_loc = fileInput(f_root,30,85)
        user_file_but.place(x=140, y = 85)

        #Original File
        org_music_l = Label(f_root , text= "Original File : " , bg="paleturquoise" , font= ("times  12 bold"))
        org_music_l.place(x = 30,y=148)
        org_file_but = Button(f_root , text= "Browse",command=lambda : fileInput(f_root,30,148))
        orgMusic_file_loc = fileInput(f_root,30,148)
        org_file_but.place(x=140, y = 148)

        
        # Plot and Compare button
        plot_and_compare_button = Button(f_root, text="Plot and Compare",command=graphWin)
        plot_and_compare_button.place(x=170, y = 220)
        

        #Function for going back to Command Window
        def back():
            f_root.destroy()

        #Back Button
        back_b=Button( f_root ,text="<--- Go Back",bd=6,command=back , fg = "black")
        back_b.place(x=6, y=230)
            

#---------------- Graph Input Win ------------------- #

def graphWin():
        # Defining File path Variables
        global user_file_loc
        global orgMusic_file_loc

        if user_file_loc == "" or orgMusic_file_loc == "":
              messagebox.showerror("Missing Inputs","Please provide both the files.")

        else:
            #Configuring Main Window
            grp_root = Toplevel(cnd_root) 
            grp_root.grab_set()
            grp_root.geometry("450x460")
            grp_root.configure(bg="paleturquoise")
            grp_root.resizable(False,False)
            grp_root.geometry("1500x760") 
            grp_root.title("Graph Input")

            #Graph Window Header Frame
            grp_h_fr=Frame(grp_root, bg="paleturquoise" )
            grp_h_fr.pack(side=TOP, fill = X)

            # Label for graph Window
            grp_text=Label(grp_h_fr, text="GRAPH" , bg="paleturquoise" , fg = "red", font= ("Posterama  40"), pady= 10)
            grp_text.pack()
            
            #Label to show which file has higher pitch
            result_text = Label(grp_root, text="" , bg="paleturquoise" ,fg = "green",  font= ("Posterama  20"))
            result_text.pack()               

            
            #Code execution and selection.
            try:    
                    fig = backend.plot_audio_files(user_file_loc,orgMusic_file_loc) 
                    backend.similarity_and_pitch(result_text,user_file_loc,orgMusic_file_loc)

            except:
                    fig = backend.plot_audio_files(user_file_loc,orgMusic_file_loc) 


            #Placing  Matplotlib Graph in Tkinter GUI Window using canvas

            canvas = FigureCanvasTkAgg(fig, master = grp_root)
            canvas.draw()
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            
            #Placing  Matplotlib Graph Toolbar in Tkinter GUI Window using canvas

            toolbar = NavigationToolbar2Tk(canvas , grp_root)
            toolbar.update()
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

                
            #Function for going back to Login Win
            def back():
                grp_root.destroy()

            #Back Button
            back_b=Button(grp_root ,text="<--- Go Back",bd=6,command=back , fg = "red")
            back_b.place(x=660, y= 720 )
        

# ---------------------- Acknowledgement Window ------------------------#

        def ackWin():
               
                clearWin(grp_root)
                grp_root.geometry("400x300")
                grp_root.title("Acknowledgement")

                # Graph Window Header Frame
                ack_h_fr = Frame(grp_root, bg="paleturquoise")
                ack_h_fr.pack(fill=X)
                

                # Thank You Label for Acknowledgement Window
                thanks_l = Label(ack_h_fr, text="Thank You!!!\n\n\n\nFor using our software." , 
                                bg="paleturquoise", fg="red", font=("Posterama  20") , pady =60)
                thanks_l.pack()

                # Message box
                messagebox.showinfo("Work In progress","This Program is still under development.")   

        # Creating Close Button    
        log_b = Button(grp_root, fg="red", text = "CLOSE"  ,font = "raleway 12 bold", command = ackWin)
        log_b.place(x=780, y=720)


# ------------------- Main Window ---------------------- #

#Window Properties
win_root = Tk() 
signUp_win = None
win_root.geometry("450x460")
win_root.configure(bg="paleturquoise")
win_root.resizable(False,False)
win_root.title("Swara")

#Global Variables
# user_file_loc = ""
# orgMusic_file_loc = ""

user_file_loc = StringVar()
orgMusic_file_loc = StringVar()


#Variables for storing Login details 
uservalue = StringVar()
passvalue = StringVar()

#Variables for storing Signup details
user_create_mobile= StringVar()
user_create_email= StringVar()
user_create_username= StringVar()
user_create_password= StringVar()
user_create_firstname= StringVar()
user_create_lastname= StringVar()
user_create_dob= StringVar()

#Objects
database = Swara_Database.Database()
backend = Swara_Backend.Backend()

#Welcome Text frame
wel_fr=Frame(win_root, bg="paleturquoise" )
wel_fr.pack(side=TOP, fill = X)

#Welcome Label
wel_text=Label(wel_fr, bg = "paleturquoise" , text="SWARA", fg = "red", font= ("Posterama  40 bold"), padx = 200 , pady=10)
wel_text.pack()

#Import image
sw_photo = PhotoImage(file="Images\logo.png")
sw_image = Label(image=sw_photo,bg = "paleturquoise")
sw_image.place(x = 230,y = 200,anchor="center")


#Start Button
start_b = Button(win_root, text = "START",font = " arial 20 bold", width = 10, height= 2, bd = 5 
                  ,fg="red" , command =  loginWin)
start_b.place(x = 230,y = 380,anchor='center')

# Creates a loop. To re-execute tkinter gui again and again.
win_root.mainloop()
