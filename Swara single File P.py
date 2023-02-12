from tkinter import *
from tkinter import ttk, filedialog
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  
# Canvas For imposing matplotlib graph with tkinter gui.
from matplotlib.figure import Figure
from tkinter.filedialog import askopenfile
import os
from tkinter import filedialog
import matplotlib.pyplot as plt
import pyaudio
import wave
import numpy as np


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
        file_h_fr=Frame(win_root, bg ="paleturquoise" )
        file_h_fr.pack(side=TOP, fill = X)

        #Header Text
        file_h_text=Label(file_h_fr, text="File Input" ,bg="paleturquoise", fg = "red", font= ("Posterama  20 bold"), padx = 200)
        file_h_text.pack()

        #Instruction Text
        inst_l = Label(win_root,text="Input your recorded music file and Original Music File Here.",
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
        user_file_l = Label(win_root , text= "Your Music File :   " , bg="paleturquoise")
        user_file_l.place(x= 30 , y = 85)
        user_file_but = Button(win_root , text= "Browse",command=lambda : fileInput(120,85))
        user_file_but.place(x=120, y = 85)
        user_file_loc = filePath
        
 

        #Original File
        org_music_l = Label(win_root , text= "Original File : " , bg="paleturquoise")  
        org_music_l.place(x = 30,y=140)
        org_file_but = Button(win_root , text= "Browse",command=lambda : fileInput(120,140))
        org_file_but.place(x=120, y = 140)
        orgMusic_file_loc = filePath
        
        #Process Button
        process_b = Button(win_root, fg="red", text = "Process"  ,font = "raleway 12 bold" , command=graphWin)
        process_b.place(x = 110, y = 210)

        print(user_file_loc,orgMusic_file_loc,sep="\n")
        


#---------------- Graph Input Win ------------------- #
def graphWin():
                          
        clearWin(win_root)
        win_root.geometry("1400x600") 
        win_root.configure(bg="paleturquoise")
        win_root.title("Graph Input")

        #Graph Window Header Frame

        grp_h_fr=Frame(win_root, bg="paleturquoise" )
        grp_h_fr.pack(side=TOP, fill = X)

        # Label for graph Window

        grp_text=Label(grp_h_fr, text="GRAPH" , bg="paleturquoise" , fg = "red", font= ("Posterama  40"))
        grp_text.pack()


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
                
                # Results of pitch comparision

        result_text = tk.Label(win_root, text="" , bg="paleturquoise" ,fg = "green",  font= ("Posterama  20"))
        result_text.pack()               


        #Python Backend Programming for file input and graph comparision.

        FRAMES_PER_BUFFER = 3200
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 16000

        audio = pyaudio.PyAudio()

        record = audio.open(
                format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=FRAMES_PER_BUFFER
        )

        print("Welcome  to SWARA!")
        print()
        print("How can I help you!")
        print()
        print("Press 1 to start recording the song you want to compare.\nPress 2 to upload the song you want to compare.")
        print()
        user_choice= int(input("Enter your choice : "))
        print()

        if (user_choice==1):      
                print('START RECORDING')
                seconds = 8
                frames = []
                second_tracking = 0
                second_count = 0
                for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
                        data = record.read(FRAMES_PER_BUFFER)
                        frames.append(data)
                        second_tracking += 1

                        if second_tracking == RATE/FRAMES_PER_BUFFER:
                                second_count += 1
                                second_tracking = 0
                                print(f'Time Left: {seconds - second_count} seconds')


                record.stop_stream()
                record.close()
                audio.terminate()

                specimen = wave.open('user.wav', 'wb')
                specimen.setnchannels(CHANNELS)
                specimen.setsampwidth(audio.get_sample_size(FORMAT))
                specimen.setframerate(RATE)
                specimen.writeframes(b''.join(frames))
                specimen.close()

                file_spec = wave.open('user.wav', 'rb')
                sample_freq = file_spec.getframerate()
                frames = file_spec.getnframes()
                signal_wave = file_spec.readframes(-1)
                file_spec.close()

        else:
                #
                print()
                file_path1 = input('Enter Recorded file path: ')
                file_spec = wave.open(file_path1, 'rb')
                sample_freq = file_spec.getframerate()
                frames = file_spec.getnframes()
                signal_wave = file_spec.readframes(-1)
    
                file_spec.close()


        time = frames / sample_freq

        # if one channel use int16, if 2 use int32
        arr = np.frombuffer(signal_wave, dtype=np.int16)
        times = np.linspace(0, time, num=frames)

        #ORIGINAL FILE EXPERIMENTAL CODE

        #user input of original file
        print()
        file_path = input('Enter Original file path: ')
        file_real = wave.open(file_path, 'rb')
        sample_freq = file_real.getframerate()
        frames = file_real.getnframes()
        signal_wave = file_real.readframes(-1)

        file_real.close()

        time = frames / sample_freq

        # if one channel use int16, if 2 use int32
       
        def plot_graph():
               
                arr2 = np.frombuffer(signal_wave, dtype=np.int16)
                times2 = np.linspace(0, time, num=frames)
                fig =  Figure(figsize=(15, 5))
                # fig = Figure(figsize=(5, 4), dpi=100)
                ax = fig.add_subplot(111)
                ax.plot(times, arr , color = 'red')
                ax.plot(times2,arr2, color = 'orange')
                plt.ylabel('Sound Wave')
                plt.xlabel('Time (s)')
                plt.xlim(0, time)
                plt.title('Graph of the specimen and original song')
                # Compare pitch
                signal1_pitch = np.mean(np.abs(np.diff(arr2)))
                signal2_pitch = np.mean(np.abs(np.diff(times2)))

                if signal1_pitch > signal2_pitch:
                        result_text.config(text=result_text.cget("text") + "\nFile 1 has higher pitch.")
                elif signal1_pitch < signal2_pitch:
                        result_text.config(text=result_text.cget("text") + "\nFile 2 has higher pitch.")
                else:
                        result_text.config(text=result_text.cget("text") + "\nBoth files have the same pitch.")

                return fig



# ------------------------------------*---------------------------------- #

        # Creting the graph holding frame
        grpframe = tk.Frame(win_root , bg ="paleturquoise")
        grpframe.pack(side=tk.LEFT)
        
        
         # Add the first graph to the first frame
        fig1 = plot_graph()
        canvas1 = FigureCanvasTkAgg(fig1, master=grpframe)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
               

        # Creating close button    
        log_b = Button(win_root, fg="red", text = "CLOSE"  ,font = "raleway 12 bold", command = ackWin)
        log_b.place(x=650, y=560)

        

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


# --------------- Main Window --------------------- #

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

wel_fr=Frame(win_root, bg="paleturquoise" )
wel_fr.pack(side=TOP, fill = X)

#Welcome Label

wel_text=Label(wel_fr, bg = "paleturquoise" , text="SWARA", fg = "red", font= ("Posterama  40 bold"), padx = 200)
wel_text.pack()

#Import image

sw_photo = PhotoImage(file="D:/Coding/Python Programming/Swara source code/logo.png")
sw_image = Label(image=sw_photo)
sw_image.place(x = 230,y = 200,anchor="center")


#Start Button

start_b = Button(win_root, text = "START",font = " arial 20 bold", width = 10, height= 2, bd = 5 
                  ,fg="red" , command =  loginWin)
start_b.place(x = 230,y = 380,anchor='center')


win_root.mainloop()
