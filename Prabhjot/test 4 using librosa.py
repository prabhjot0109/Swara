import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
import librosa

def open_file():
    file_path = filedialog.askopenfilename()
    return file_path

def plot_superimposed_audio(audio1, audio2):
    fig, ax = plt.subplots()
    ax.plot(audio1, label='Audio 1')
    ax.plot(audio2, label='Audio 2')
    ax.legend()
    plt.show()

def compare_pitch(audio1, audio2):
    audio1_pitch = librosa.estimate_tuning(y=audio1, sr=sr)
    audio2_pitch = librosa.estimate_tuning(y=audio2, sr=sr)

    pitch_diff = abs(audio1_pitch - audio2_pitch)
    similarity = 100 - (pitch_diff / audio1_pitch * 100)

    return similarity

def process_audio():
    file1_path = open_file()
    file2_path = open_file()

    audio1, sr = librosa.load(file1_path)
    audio2, sr = librosa.load(file2_path)

    plot_superimposed_audio(audio1, audio2)

    similarity = compare_pitch(audio1, audio2)
    result_label.config(text=f'Similarity: {similarity:.2f}%')

root = tk.Tk()
root.title("Audio Comparison")

open_file_button = tk.Button(root, text="Open Files", command=process_audio)
open_file_button.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()
