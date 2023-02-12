import tkinter as tk
import wave
import matplotlib.pyplot as plt
import numpy as np
import struct
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

def open_file():
    file_path = filedialog.askopenfilename()
    return file_path

def compare_audio(audio1, audio2):
    distance, path = fastdtw(audio1, audio2, dist=euclidean)
    similarity = 1 - distance / max(len(audio1), len(audio2))
    
    return similarity

def process_audio():
    file1_path = open_file()
    file2_path = open_file()

    with wave.open(file1_path, 'r') as f:
        sr = f.getframerate()
        audio1 = np.array([struct.unpack("<h", f.readframes(1))[0] for i in range(f.getnframes())])
    with wave.open(file2_path, 'r') as f:
        sr = f.getframerate()
        audio2 = np.array([struct.unpack("<h", f.readframes(1))[0] for i in range(f.getnframes())])

    fig, ax = plt.subplots()
    ax.plot(audio1, label='Audio 1')
    ax.plot(audio2, label='Audio 2')
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    similarity = compare_audio(audio1, audio2)
    result_label.config(text=f'Similarity: {similarity:.2f}')

root = tk.Tk()
root.title("Audio Comparison")

open_file_button = tk.Button(root, text="Open Files", command=process_audio)
open_file_button.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()
