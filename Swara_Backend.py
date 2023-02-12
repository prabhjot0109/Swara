import tkinter as tk
import wave
import matplotlib.pyplot as plt
import numpy as np
from tkinter import filedialog

def plot_audio_files(user_file, org_file):
    # Load audio files
    with wave.open(user_file, "rb") as wav_user_file:
        user_X = wav_user_file.readframes(wav_user_file.getnframes())
        user_sr = wav_user_file.getframerate()

    with wave.open(org_file, "rb") as wav_org_file:
        org_X = wav_org_file.readframes(wav_org_file.getnframes())
        org_sr = wav_org_file.getframerate()

    # Convert audio files to numpy arrays
    user_X = np.frombuffer(user_X, dtype=np.int16)
    org_X = np.frombuffer(org_X, dtype=np.int16)

    # Plot superimposed audio files
    plt.figure(figsize=(15, 7))
    plt.plot(user_X, label=user_file, color= "red", zorder = 0.4)
    plt.plot(org_X, label=org_file , color = "orange", alpha = 0.8)
    plt.xlim(0, len(user_X))
    plt.legend()
    plt.show()

def similarity_and_pitch(text, user_file, org_file):
    # Load audio files
    #User
    with wave.open(user_file, "rb") as wav_user_file:
        user_X = wav_user_file.readframes(wav_user_file.getnframes())
        user_sr = wav_user_file.getframerate()

    with wave.open(org_file, "rb") as wav_org_file:
        org_X = wav_org_file.readframes(wav_org_file.getnframes())
        org_sr = wav_org_file.getframerate()
    
    # Convert audio files to numpy arrays
    user_X = np.frombuffer(user_X, dtype=np.int16)
    org_X = np.frombuffer(org_X, dtype=np.int16)
    # Compare pitches

    # Compare pitches
    if np.mean(user_X) > np.mean(org_X):
        pitch_comparison = 'Signal 1 has  higher pitch.'
    elif np.mean(user_X) < np.mean(org_X):
        pitch_comparison = 'Signal 2 has higher pitch.'
    else:
        pitch_comparison = 'The signals have the same pitch'

    # Calculate similarity percentage
    similarity = np.corrcoef(user_X, org_X)[0, 1] * 100
    similarity = round(similarity, 2)

    # Display results
    # text.config(text=f"Pitch Comparison: {pitch_comparison}\nSimilarity: {similarity}%")
    text.config(text=f"Pitch Comparison: {pitch_comparison}")
    

