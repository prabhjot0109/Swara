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
import time

# Importing Custom Files
import Swara_Backend
import Swara_Database


#Functionality Class

class Functionality:
    #Function for clearing Win

    def clearWin(self,window):
        for widgets in window.winfo_children():
            widgets.destroy()

    #Function for taking File Input 
    def fileInput(self,win,evar,b_x,b_y):
            self.file = filedialog.askopenfile(mode='r', filetypes=[('Music Files', '*.wav')])
            
            if self.file:
                    self.filePath = os.path.abspath(self.file.name)
                    self.path = self.filePath
                    self.file_loc_e = Entry(win ,textvar = evar,font = "raleway 10 bold", bg="#1b191a",bd = 0,width = 200)
                    self.file_loc_e.delete(first = 0,last = 500)
                    self.file_loc_e.insert(0,f"{self.filePath}")
                    self.file_loc_e.config(state = "disabled" ,  bg="#1b191a")
                    self.file_loc_e.place(x = b_x, y = (b_y + 30))                        
                    return self.path

    #Function for recording Audio
    def recording(self,win,sec_e):
        self.sec = sec_e.get()
        self.FRAMES_PER_BUFFER = 3200
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 16000

        # Calling Python library to record audio
        self.audio = pyaudio.PyAudio()

        self.record = self.audio.open(
                format=self.FORMAT,
                channels=self.CHANNELS,
                rate=self.RATE,
                input=True,
                frames_per_buffer=self.FRAMES_PER_BUFFER
        )
        
        # Creates a label when recording completes.
        self.ch2 = Label(win , text= "Your voice is Recorded!" ,bg = "#141a1a" , fg="#f3b32d" ,font= ("Posterama  16 bold"))
        self.ch2.place(x= 140 , y = 220)

        # Defines recording interval by taking input from user.

        self.seconds = float(self.sec)
        self.frames = []
        self.second_tracking = 0
        self.second_count = 0
        for i in range(0, int(self.RATE/self.FRAMES_PER_BUFFER*self.seconds)):
                self.ch3 = Label(win, textvariable = f'Time Left: {self.seconds - self.second_count} seconds' , bg="#1b191a")
                self.ch3.place(x= 30 , y = 130)
                self.data = self.record.read(self.FRAMES_PER_BUFFER)
                self.frames.append(self.data)
                self.second_tracking += 1
                self.second_count += 1


        self.record.stop_stream()
        self.record.close()
        self.audio.terminate()

        # Stores recorded audio file.

        specimen = wave.open('Audio/user.wav', 'wb')
        specimen.setnchannels(self.CHANNELS)
        specimen.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        specimen.setframerate(self.RATE)
        specimen.writeframes(b''.join(self.frames))
        specimen.close()

        

# Button bg - #141a1a (Lighter Black)
# Button Text - deeppink 
# bg - #1b191a (Black)
# fontcolour - #f3b32d (Golden Colour)

#-------------------- Login Win -------------------- #

def loginWin():
        functionality.clearWin(win_root)

        win_root.geometry("260x200")
        win_root.config(bg = "#1b191a")

        #Login Win Header Frame
        login_h_fr=Frame(win_root, bg="#1b191a",bd = 2)
        login_h_fr.pack(side=TOP, fill = X)

        #Login Label
        login_text=Label(login_h_fr, text="LOGIN" ,bg="#1b191a", fg = "#f3b32d", font= ("Posterama  20 bold"), padx = 200 , pady = 10)
        login_text.pack()

        #User
        user = Label(win_root , text= "Username ID  :   ", bg="#1b191a" , fg="#f3b32d")
        user.place(x= 30 , y = 58)

        userEntry = Entry(win_root , textvariable =uservalue )
        userEntry.place(x=120, y = 58)

        #Password
        password = Label(win_root , text= "Password : ", bg="#1b191a" , fg="#f3b32d")  
        password.place(x = 30,y=80)

        passEntry = Entry(win_root , textvariable = passvalue, show = "*")
        passEntry.place(x=120 ,y = 80)
        
        #Login Button
        login = lambda:database.login(userEntry,passEntry,chooseWin)  
        log_b = Button(win_root, fg="deeppink", bg = "#141a1a", text = "Login"  ,font = "raleway 12 bold", command = login) #Checks and verify the login details
        log_b.place(x = 160, y = 130)

        #Create User Button
        c_user_b = Button(win_root,fg = "deeppink",bg = "#141a1a", text = "Sign - Up", font = "raleway 12 bold" ,command= createUserWin)
        c_user_b.place(x = 30, y = 130)


#----------------------------Sign Up window----------------------#

def createUserWin():

    global signUp_win

    #Window Properties
    signUp_win = Toplevel(win_root)
    signUp_win.geometry("410x500")
    signUp_win.resizable(False,False)
    signUp_win.title("Sign - Up")    
    signUp_win.configure(bg="#1b191a")  
    signUp_win.grab_set()



    #Heading Frame
    h_frame= Frame(signUp_win , bg="#1b191a" ,bd=10)
    h_frame.grid(row=0,column=0)
    h= Label(h_frame ,text="Create Account",font=("Times 20 bold") , bg="#1b191a" , fg="#f3b32d")
    h.grid(padx=100,pady=2)

    #Details Frame
    details_frame= Frame(signUp_win , bg="#1b191a")
    details_frame.grid(row=1,column=0)

    #Mobile No.
    mobile_no_l= Label(details_frame,text="Mobile Number : " , bg="#1b191a" , fg="#f3b32d")      
    mobile_no_l.grid(row=0,column=0,padx=5,pady=10)
    user_create_mobile.set("")
    
    mobile_no_e= Entry(details_frame,width=20,justify="center",textvariable=user_create_mobile)
    mobile_no_e.config(state="normal")
    mobile_no_e.grid(row=0,column=1)

    #E-mail
    email_l= Label(details_frame,text="Email Address : " , bg="#1b191a", fg="#f3b32d")
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
    check_b = Button(details_frame,text="Check", command = check_me ,bg = "#141a1a",  fg="deeppink" ,  font= ("times  10 bold"))
    check_b.grid(row=1,column=2,padx=10)
    
    #Username
    username_l= Label(details_frame,text="Username : " , bg="#1b191a", fg="#f3b32d")
    username_l.grid(row=2,column=0,padx=5,pady=10,sticky='w')
    user_create_username.set("")
    
    username_e= Entry(details_frame,width=20,justify="center",textvariable=user_create_username)
    username_e.grid(row=2,column=1)
    username_e.config(state="disabled")

    #Password
    password_l= Label(details_frame,text="Password : " , bg="#1b191a" , fg="#f3b32d")
    password_l.grid(row=3,column=0,padx=5,pady=10,sticky='w')
    user_create_password.set("")
    
    password_e= Entry(details_frame,width=20,justify="center",show = "*",textvariable=user_create_password)
    password_e.grid(row=3,column=1)
    password_e.config(state="disabled")

    #First Name
    first_name_l= Label(details_frame,text="First Name : " , bg="#1b191a" , fg="#f3b32d")
    first_name_l.grid(row=4,column=0,padx=5,pady=10,sticky='w')
    user_create_firstname.set("")
    
    first_name_e= Entry(details_frame,width=20,justify="center",textvariable=user_create_firstname)
    first_name_e.grid(row=4,column=1)
    first_name_e.config(state="disabled")

    #Last Name
    last_name_l= Label(details_frame,text="Last Name : " , bg="#1b191a" , fg="#f3b32d")
    last_name_l.grid(row=5,column=0,padx=5,pady=10,sticky='w')
    user_create_lastname.set("")
    
    last_name_e= Entry(details_frame,width=20,justify="center",textvariable=user_create_lastname)
    last_name_e.grid(row=5,column=1)
    last_name_e.config(state="disabled")

    #DOB
    dob_l= Label(details_frame,text="Date Of Birth : " , bg="#1b191a" , fg="#f3b32d")
    dob_l.grid(row=6,column=0,padx=5,pady=10,sticky='w',columnspan=2)
    
    date_l= Label(details_frame , bg="#1b191a")
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
            date_l.config(text=dob_e.get_date(), fg="#f3b32d")
            user_create_dob.set(dob_e.get_date())                    
            date_picker.destroy()
        
        #Ok Button
        ok= Button(date_picker,text="OK",bd=5,command=picked , fg= "deeppink" ,bg = "#141a1a")
        ok.pack(pady=10)           

    #Choose Button
    choose= Button(details_frame,text="Choose Date",command=choose_date, bg = "#141a1a", fg="deeppink", font= ("times  10 bold"))
    choose.grid(row=6,column=2)
    choose.config(state="disabled")
    choose.config(state="disabled")

   
    #Sumbit Button
    submit = lambda : database.regSumbit(signUp_win, user_create_email, user_create_mobile,user_create_username,user_create_password,user_create_firstname,user_create_lastname,user_create_dob ) 
    submit_b =Button( signUp_win , text="SUBMIT",width=10,bd=6,font= ("Posterama  20 bold"), command = submit , fg = "deeppink", bg = "#141a1a")
    submit_b.config(state="disabled")
    submit_b.place(x=100 , y=360)


    #Function for going back to Login Win
    def back():
        signUp_win.destroy()

    #Back Button
    back_b=Button(signUp_win ,text="<--- Go Back to Login",bd=6,command=back , fg = "deeppink" ,bg = "#141a1a")
    back_b.place( x= 6 , y= 450 )
        

#-----------------Choose option window---------------#

def chooseWin():

        global cnd_root

        #Command Window Properties
        cnd_root = Toplevel(win_root)
        cnd_root.grab_set() 
        cnd_root.configure(bg="#1b191a")
        cnd_root.resizable(False,False)
        cnd_root.title("Option Window")
        cnd_root.geometry("280x200")

        #Command Win Header Frame
        ch_h_fr=Frame(cnd_root, bg="#1b191a" )
        ch_h_fr.pack(side=TOP, fill = X)

        #Command Label
        ch_text=Label(ch_h_fr, text="COMMAND" ,bg="#1b191a", fg="#f3b32d", font= ("Posterama  20 bold"), padx = 200 , pady= 20)
        ch_text.pack()
        
        #Upload Button
        up_b = Button(cnd_root, fg="deeppink" , bg = "#141a1a" ,text = "Upload File", font = " raleway 12 bold" , command = fileWin)
        up_b.place(x = 20, y = 90)

        #Record Button
        rec_b = Button(cnd_root , fg="deeppink",  bg = "#141a1a", text = "Record Audio"  ,font = "raleway 12 bold", command = recordWin )
        rec_b.place(x = 140, y = 90)

        #Function for going back to Login Window

        def back():
                cnd_root.destroy()

        #Back Button
        back_b=Button(cnd_root, text="<--- Go Back to Login",bd=6,command=back , fg="deeppink",  bg = "#141a1a")
        back_b.place(x=6 , y=160 )  


#-----------------Record audio window---------------#

def recordWin():
    
    global rec_root
    global orgMusic_file_loc
    global user_file_loc

    #Record Win Configurations
    rec_root = Toplevel(cnd_root) 
    rec_root.grab_set()
    rec_root.geometry("520x450")
    rec_root.configure(bg="#1b191a")
    rec_root.resizable(False,False)
    rec_root.title("Record Audio")

    # Defining files path variables

    cwd = os.getcwd()
    user_file_loc = cwd + r"\Audio\user.wav"

    #user_file_loc = "Audio/user.wav"

    #Command Win Header Frame
    ch_h_fr=Frame(rec_root, bg="#1b191a" )
    ch_h_fr.pack(side=TOP, fill = X)
        
    #Command Label
    ch_text=Label(ch_h_fr, text="Record Audio" ,bg="#1b191a", fg="#f3b32d", font= ("Posterama  25 bold"), padx = 200 , pady= 10)
    ch_text.pack()

    # Original File upload label
    org_music_l = Label(rec_root , text= "Original File : " , bg="#1b191a",  fg="#f3b32d", font= ("Posterama  12 bold"))
    org_music_l.place(x= 20 , y= 80)
    orgMusic_file_loc = functionality.fileInput(rec_root,orgMusic_file_loc_evar,20,80)
    org_file_but = Button(rec_root , bg = "#141a1a" , fg= "deeppink",  text= "Browse",command=lambda : functionality.fileInput(rec_root,20 , 80))#(120,140))
    org_file_but.place(x= 165 , y= 80)
    
    #Interval input label
    interval_l = Label(rec_root , text= "Enter recording interval : \n(in Seconds)  " , fg="#f3b32d", bg="#1b191a",  font= ("Posterama  12 bold"))
    interval_l.place(x= 35 , y= 150)

    # Interval input entry box
    sec_e = Entry(rec_root,font = "Posterama 15 bold", width = 10)
    sec_e.place(x= 260 , y= 150)
    

    # Record Audio button
    record_button = Button(rec_root, text="Record Audio",bg = "#141a1a" , fg= "deeppink"  , command= lambda : functionality.recording(rec_root,sec_e) , font = " arial 15 bold", width = 14, height= 2,
                relief = RAISED) 
    record_button.place(x=170 , y=260)

    # Plot and compare button
    next_button = Button(rec_root, text ="Plot and Compare", command=graphWin ,font = " arial 15 bold", width = 16, height= 2
                , bg = "#141a1a" , fg= "deeppink"  , relief = RAISED )
    next_button.place(x= 160 , y= 350)
    
    #Function for going back to Command Window
    def back():
        rec_root.destroy()
        
    #Back Button
    back_b=Button(rec_root ,text="<--- Go Back", bg = "#141a1a" , fg= "deeppink" ,bd=6,command=back )
    back_b.place(x= 10 , y=400)
  


#------------------ File Input Win -------------------#

def fileWin():

        global f_root

        #File Input Win Configuration        
        f_root = Toplevel(cnd_root)
        f_root.grab_set() 
        f_root.configure(bg="#1b191a")
        f_root.resizable(False,False)
        f_root.title("File Input")
        f_root.geometry("600x270")
        
        # Defining file path variables
        global user_file_loc
        global orgMusic_file_loc

        #File Header Frame
        file_h_fr=Frame(f_root, bg ="#1b191a" )
        file_h_fr.pack(side=TOP, fill = X)

        #Header Text
        file_h_text=Label(file_h_fr, text="File Input" ,bg="#1b191a", fg="#f3b32d",
                          font= ("Posterama  20 bold"), padx = 200 , pady = 10)
        file_h_text.pack()

        #Instruction Text
        inst_l = Label(f_root,text="Input your recorded music file and Original Music File Here.",
                        bg="#1b191a" , fg="#f3b32d", font = ("Posterama  12 bold") )
        inst_l.pack()

        #User File
        user_file_l = Label(f_root , text= "Recorded File :   " , bg="#1b191a" , fg="#f3b32d",  font= ("times  12  bold"))
        user_file_l.place(x= 30 , y = 85)
        user_file_but = Button(f_root ,bg = "#141a1a", fg="deeppink" , text= "Browse",command=lambda : functionality.fileInput(f_root,user_file_loc_evar,30,85))
        user_file_loc = functionality.fileInput(f_root,user_file_loc_evar,30,85)
        user_file_but.place(x=140, y = 85)

        #Original File
        org_music_l = Label(f_root , text= "Original File : " ,  fg="#f3b32d", bg="#1b191a" , font= ("times  12 bold"))
        org_music_l.place(x = 30,y=148)
        org_file_but = Button(f_root , fg="deeppink"  ,bg = "#141a1a", text= "Browse",command=lambda : functionality.fileInput(f_root,orgMusic_file_loc_evar,30,148))
        orgMusic_file_loc = functionality.fileInput(f_root,orgMusic_file_loc_evar,30,148)
        org_file_but.place(x=140, y = 148)

        
        # Plot and Compare button
        plot_and_compare_button = Button(f_root, bg = "#141a1a" , fg= "deeppink" , text="Plot and Compare",command=graphWin)
        plot_and_compare_button.place(x=240, y = 220)
        

        #Function for going back to Command Window
        def back():
            f_root.destroy()

        #Back Button
        back_b=Button( f_root ,text="<--- Go Back", bg = "#141a1a" , fg= "deeppink" ,bd=6,command=back )
        back_b.place(x=6, y=230)
            

#---------------- Graph Input Win ------------------- #

def graphWin():

    # Defining File path Variables
    global user_file_loc
    global orgMusic_file_loc
    global grp_root

    #Configuring Main Window
    grp_root = Toplevel(cnd_root) 
    grp_root.grab_set()
    grp_root.geometry("450x460")
    grp_root.configure(bg="white")
    grp_root.resizable(False,False)
    grp_root.geometry("1500x760") 
    grp_root.title("Graph Input")

    #Graph Window Header Frame
    grp_h_fr=Frame(grp_root, bg="white" )
    grp_h_fr.pack(side=TOP, fill = X)

    # Label for graph Window
    grp_text=Label(grp_h_fr, text="GRAPH" , bg="white" ,  fg="#f3b32d", font= ("Posterama  40"), pady= 10)
    grp_text.pack()
    
    #Label to show which file has higher pitch
    result_text = Label(grp_root, fg="deeppink", bg= "white",  font= ("Posterama  20"))
    result_text.pack()               

    #Code execution and selection.
    try:    
            fig = backend.plot_audio_files(user_file_loc_evar,orgMusic_file_loc_evar,user_file_loc) 
            backend.similarity_and_pitch(result_text)

    except:
            fig = backend.plot_audio_files(user_file_loc_evar,orgMusic_file_loc_evar,user_file_loc) 


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
    back_b=Button(grp_root ,text="<--- Go Back", bg = "white" , fg= "deeppink" ,bd=6,command=back )
    back_b.place(x=660, y= 720 )
        

# ---------------------- Acknowledgement Window ------------------------#
    def ackWin():
            
        functionality.clearWin(grp_root)
        grp_root.geometry("400x300")
        grp_root.title("Acknowledgement")

        # Graph Window Header Frame
        ack_h_fr = Frame(grp_root, bg="#1b191a")
        ack_h_fr.pack(fill=X)

        # Thank You Label for Acknowledgement Window
        thanks_l = Label(ack_h_fr, text="Thank You!!!\n\n\n\nFor using our software." , 
                        bg="#1b191a", fg="#f3b32d", font=("Posterama  20") , pady =60)
        thanks_l.pack()

        win_root.destroy()

    # Creating Close Button    
    log_b = Button(grp_root, bg = "white" , fg= "deeppink" , text = "CLOSE"  ,font = "raleway 12 bold", command = ackWin)
    log_b.place(x=780, y=720)


# ------------------- Main Window ---------------------- #

#Windows 
win_root = Tk() 
signUp_win = None
grp_root = None

#Main Window Properties
win_root.geometry("460x450")
win_root.resizable(False,False)
win_root.title("Swara")


# Global Variables
user_file_loc = ""
orgMusic_file_loc = ""

user_file_loc_evar = StringVar()
orgMusic_file_loc_evar = StringVar()


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
functionality = Functionality()


#Import image
sw_photo = PhotoImage(file=r"Images\front.png")
sw_image = Label(image=sw_photo)
sw_image.pack(anchor="center" )

#Start Button
start_img = PhotoImage(file = r"Images\btn.png")
start_b = Button(win_root,image = start_img   , fg="red" , bg = "#1b191a",  command =  loginWin , relief = "flat") 
# Relief = flat, groove, raised, ridge, solid, or sunken
                
#start_b = Button(win_root, text = "START",font = " arial 20 bold", width = 6 ,  fg="deeppink" , command =  loginWin)    
start_b.place(x = 84 ,y =15)

# Creates a loop. To re-execute tkinter gui again and again.
win_root.mainloop()
