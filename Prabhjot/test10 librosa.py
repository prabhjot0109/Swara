import matplotlib.pyplot as plt
import numpy as np
import wave
import librosa
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def compare_audio_files():
    # Load audio files
    file1 = wave.open("file1.wav", "rb")
    file2 = wave.open("file2.wav", "rb")

    # Extract audio data
    data1 = file1.readframes(file1.getnframes())
    data2 = file2.readframes(file2.getnframes())

    # Convert to numpy arrays
    audio1 = np.frombuffer(data1, dtype=np.int16)
    audio2 = np.frombuffer(data2, dtype=np.int16)

    # Calculate MFCCs
    mfcc1 = librosa.feature.mfcc(y=audio1, sr=file1.getframerate(), n_mfcc=13)
    mfcc2 = librosa.feature.mfcc(y=audio2, sr=file2.getframerate(), n_mfcc=13)

    # Plot MFCCs
    plt.figure()
    plt.plot(mfcc1.T, label='File 1')
    plt.plot(mfcc2.T, label='File 2')
    plt.legend()

    # Create Tkinter GUI
    root = tk.Tk()
    canvas = FigureCanvasTkAgg(plt.gcf(), master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    tk.mainloop()

if __name__ == '__main__':
    compare_audio_files()
