import tkinter as tk
import wave
import matplotlib.pyplot as plt
import numpy as np
import struct
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    return file_path

def plot_superimposed_audio(audio1, audio2):
    fig, ax = plt.subplots()
    ax.plot(audio1, label='Audio 1')
    ax.plot(audio2, label='Audio 2')
    ax.legend()
    plt.show()

def compare_pitch(audio1, audio2, sr):
    def autocorrelation(signal, sr):
        signal = signal - np.mean(signal)
        corr = np.correlate(signal, signal, mode='full')
        corr = corr[len(corr)//2:]
        corr = corr / np.sum(signal**2)
        corr = corr / sr
        return corr

    audio1_corr = autocorrelation(audio1, sr)
    audio2_corr = autocorrelation(audio2, sr)

    audio1_pitch = sr / np.argmax(audio1_corr)
    audio2_pitch = sr / np.argmax(audio2_corr)

    similarity = 100 * np.abs(audio1_pitch - audio2_pitch) / ((audio1_pitch + audio2_pitch) / 2)
    
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

    plot_superimposed_audio(audio1, audio2)

    similarity = compare_pitch(audio1, audio2, sr)
    result_label.config(text=f'Similarity: {100-similarity:.2f}%')

root = tk.Tk()
root.title("Audio Comparison")

open_file_button = tk.Button(root, text="Open Files", command=process_audio)
open_file_button.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()
