# Extractes raw data from .wav audio files
import wave

# Plots graph of audio files
import matplotlib.pyplot as plt

# Converts raw data into numerical arrays for plotting
import numpy as np

# iuper Imposes graph in tkineter GUI
from matplotlib.figure import Figure
from scipy.fft import fft
from scipy.spatial.distance import cosine



#Function For plotting Audio Graphs 
def plot_audio_files(user_file, org_file):

    # Loads audio files
    with wave.open(user_file, "rb") as wav_user_file:
        user_sr = wav_user_file.getframerate()
        user_X = wav_user_file.readframes(wav_user_file.getnframes())
        

    with wave.open(org_file, "rb") as wav_org_file:
        org_sr = wav_org_file.getframerate()
        org_X = wav_org_file.readframes(wav_org_file.getnframes())
        
    # Convert audio files to numpy arrays
    user_X = np.frombuffer(user_X, dtype=np.int16)
    org_X = np.frombuffer(org_X, dtype=np.int16)
    
    user_t = np.arange(user_X.size) / user_sr
    org_t = np.arange(org_X.size) / org_sr

    # Plot waveform graph
    fig = Figure(figsize=(10, 6))
    ax = fig.add_subplot()

    ax.plot(user_t, user_X, label=user_file, color="red", alpha=0.7)
    ax.plot(org_t, org_X, label=org_file, color="green", alpha=0.7)
    
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title("Waveform of audio files")
    ax.legend()

    return fig

def calculate_accuracy(user_file, org_file):
    with wave.open(user_file, "rb") as wav_user_file:
        user_sr = wav_user_file.getframerate()
        user_X = wav_user_file.readframes(wav_user_file.getnframes())
        
    with wave.open(org_file, "rb") as wav_org_file:
        org_sr = wav_org_file.getframerate()
        org_X = wav_org_file.readframes(wav_org_file.getnframes())

    # Convert audio files to numpy arrays
    user_X = np.frombuffer(user_X, dtype=np.int16)
    org_X = np.frombuffer(org_X, dtype=np.int16)

    # Calculate mean squared error (MSE)
    mse = np.square(np.subtract(user_X, org_X)).mean()

    # Calculate maximum possible amplitude and MSE
    max_amp = 2 ** 15  # 16-bit audio
    max_mse = max_amp ** 2

    # Calculate accuracy
    accuracy = (mse / max_mse)
    
    print(accuracy)

    return accuracy


# # Function for comparing Audio Files   
# def similarity_and_pitch(text, user_file, org_file):

#     # Loads audio files
#     with wave.open(user_file, "rb") as wav_user_file:
#         user_sr = wav_user_file.getframerate()
#         user_X = wav_user_file.readframes(wav_user_file.getnframes())
      

#     with wave.open(org_file, "rb") as wav_org_file:
#         org_sr = wav_org_file.getframerate()
#         org_X = wav_org_file.readframes(wav_org_file.getnframes())
        
    
#     # Convert audio files to numpy arrays
#     user_X = np.frombuffer(user_X, dtype=np.int16)
#     org_X = np.frombuffer(org_X, dtype=np.int16)
    

#     # Compare pitches
#     if np.mean(user_X) > np.mean(org_X):
#         pitch_comparison = 'File 1 has  higher pitch.'
#     elif np.mean(user_X) < np.mean(org_X):
#         pitch_comparison = 'File 2 has higher pitch.'
#     else:
#         pitch_comparison = 'Both the files have the same pitch.'

#     # Calculate similarity percentage
#     similarity = np.corrcoef(user_X, org_X)[0, 1] * 100
#     similarity = round(similarity, 2)

#     # Displays result in tkinter GUI
#     text.config(text=f"Pitch Comparison: {pitch_comparison}\nSimilarity: {similarity}%")
    
#     text.config(text=f"Pitch Comparison: {pitch_comparison}")
#     print(pitch_comparison,similarity)

