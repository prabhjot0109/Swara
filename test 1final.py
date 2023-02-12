import tkinter as tk
import wave
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog

def plot_audio_files(user_file, org_file):
    # Load audio files
    with wave.open(user_file, "rb") as wav_user_file:
        x1 = wav_user_file.readframes(wav_user_file.getnframes())
        sr1 = wav_user_file.getframerate()

    with wave.open(org_file, "rb") as wav_org_file:
        x2 = wav_org_file.readframes(wav_org_file.getnframes())
        sr2 = wav_org_file.getframerate()

    # Convert audio files to numpy arrays
    x1 = np.frombuffer(x1, dtype=np.int16)
    x2 = np.frombuffer(x2, dtype=np.int16)

    # Plot superimposed audio files
    plt.figure(figsize=(15, 7))
    plt.plot(x1, label=user_file, color= "red", zorder = 0.8)
    plt.plot(x2, label=org_file , color = "orange", alpha = 0.6)
    plt.xlim(0, len(x1))
    plt.legend()
    plt.show()

def similarity_and_pitch(user_file, org_file):
    # Load audio files
    #User
    with wave.open(user_file, "rb") as wav_user_file:
        x1 = wav_user_file.readframes(wav_user_file.getnframes())
        sr1 = wav_user_file.getframerate()

    with wave.open(org_file, "rb") as wav_org_file:
        x2 = wav_org_file.readframes(wav_org_file.getnframes())
        sr2 = wav_org_file.getframerate()
    
    # Convert audio files to numpy arrays
    x1 = np.frombuffer(x1, dtype=np.int16)
    x2 = np.frombuffer(x2, dtype=np.int16)
    # Compare pitches

    # Compare pitches
    if np.mean(x1) > np.mean(x2):
        pitch_comparison = 'Signal 1 has  higher pitch.'
    elif np.mean(x1) < np.mean(x2):
        pitch_comparison = 'Signal 2 has higher pitch.'
    else:
        pitch_comparison = 'The signals have the same pitch'

    # Calculate similarity percentage
    similarity = np.corrcoef(x1, x2)[0, 1] * 100
    similarity = round(similarity, 2)

    # Display results
    # result_text.config(text=f"Pitch Comparison: {pitch_comparison}\nSimilarity: {similarity}%")
    result_text.config(text=f"Pitch Comparison: {pitch_comparison}")
    

# Tkinter GUI
root = tk.Tk()
root.geometry("400x200")
root.title("Audio File Comparison")

# File 1 selection
user_file_label = tk.Label(root, text="File 1")
user_file_label.pack()

user_file = tk.StringVar()
user_file_entry = tk.Entry(root, textvariable=user_file)
user_file_entry.pack()

user_file_button = tk.Button(root, text="Select File", command=lambda: user_file.set(filedialog.askopenfilename()))
user_file_button.pack()

# File 2 selection
org_file_label = tk.Label(root, text="File 2")
org_file_label.pack()

org_file = tk.StringVar()
org_file_entry = tk.Entry(root, textvariable=org_file)
org_file_entry.pack()

org_file_button = tk.Button(root, text="Select File", command=lambda: org_file.set(filedialog.askopenfilename()))
org_file_button.pack()

# Results
result_text = tk.Label(root, text="")
result_text.pack()

# Plot and Compare button
plot_and_compare_button = tk.Button(root, text="Plot and Compare", command=lambda: plot_audio_files(user_file.get(), org_file.get()) or similarity_and_pitch(user_file.get(), org_file.get()))
plot_and_compare_button.pack()

root.mainloop()
