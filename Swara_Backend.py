# Extractes raw data from .wav audio files
import wave

# Plots graph of audio files
import matplotlib.pyplot as plt

# Converts raw data into numerical arrays for plotting
import numpy as np

from tkinter import messagebox

# iuper Imposes graph in tkineter GUI
from matplotlib.figure import Figure
# from scipy.fft import fft
# from scipy.spatial.distance import cosine

class Backend :
    
    #Function For plotting Audio Graphs 
    def plot_audio_files(self,user_file_e, org_file_e):

        user_file = user_file_e.get()
        org_file = org_file_e.get()
        
        print(user_file,org_file,sep = "\n")

        if user_file == "" or org_file == "":
            messagebox.showerror("Missing Inputs","Please provide both the files.")

        else:
            # Loads audio files
            with wave.open(user_file, "rb") as self.wav_user_file:
                self.user_sr = self.wav_user_file.getframerate()
                self.user_X = self.wav_user_file.readframes(self.wav_user_file.getnframes())
                

            with wave.open(org_file, "rb") as self.wav_org_file:
                self.org_sr = self.wav_org_file.getframerate()
                self.org_X = self.wav_org_file.readframes(self.wav_org_file.getnframes())
                
            # Convert audio files to numpy arrays
            self.user_X = np.frombuffer(self.user_X, dtype=np.int16)
            self.org_X = np.frombuffer(self.org_X, dtype=np.int16)
            
            #Time = Frame Data/No. of Frames
            self.user_t = np.arange(self.user_X.size) / self.user_sr
            self.org_t = np.arange(self.org_X.size) / self.org_sr

            # Plot waveform graph
            self.fig = Figure(figsize=(5,4), dpi=100)
            self.ax = self.fig.add_subplot(111)

            self.ax.plot(self.user_t, self.user_X, label=user_file, color="red", alpha=0.7)
            self.ax.plot(self.org_t, self.org_X, label=org_file, color="green", zorder=0.6)

            plt.xlim(0, len(self.user_X))

            self.ax.set_xlabel("Time (s)")
            self.ax.set_ylabel("Amplitude")
            self.ax.set_title("Waveform of audio files")
            self.ax.legend()

            return self.fig

    # Function for comparing Audio Files   
    def similarity_and_pitch(self ,text):

        # Compare pitches
        if np.mean(self.user_X) > np.mean(self.org_X):
            self.pitch_comparison = 'File 1 has  higher pitch.'
        elif np.mean(self.user_X) < np.mean(self.org_X):
            self.pitch_comparison = 'File 2 has higher pitch.'
        else:
            self.pitch_comparison = 'Both the files have the same pitch.'

        # Calculate similarity percentage
        self.similarity = np.corrcoef(self.user_X, self.org_X)[0, 1] * 100
        self.similarity = round(self.similarity, 2)

        # Displays result in tkinter GUI

        text.config(text=f"Pitch Comparison: {self.pitch_comparison}")
        #text.config(text=f"Pitch Comparison: {self.pitch_comparison}\nSimilarity: {self.similarity}%")
        # print(pitch_comparison,similarity)

