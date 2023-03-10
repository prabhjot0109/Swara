import wave
import numpy as np
from scipy.io import wavfile
from scipy.spatial.distance import cosine

# Load the audio files
audio_file_1 = "D:\Coding\Swara-master\Audio\user_z.wav"
audio_file_2 = "D:\Coding\Swara-master\Audio\userop2.wav"

# Open the audio files and read the data
with wave.open(audio_file_1, 'rb') as f:
    params_1 = f.getparams()
    audio_data_1 = f.readframes(params_1[3])
    
with wave.open(audio_file_2, 'rb') as f:
    params_2 = f.getparams()
    audio_data_2 = f.readframes(params_2[3])

# Convert the audio data to numpy arrays
audio_array_1 = np.frombuffer(audio_data_1, dtype=np.int16)
audio_array_2 = np.frombuffer(audio_data_2, dtype=np.int16)

# Calculate the sampling rate and audio duration
sampling_rate_1, audio_duration_1 = wavfile.read(audio_file_1)
sampling_rate_2, audio_duration_2 = wavfile.read(audio_file_2)

# Check if the audio files have the same sampling rate and duration
if sampling_rate_1 != sampling_rate_2 or audio_duration_1 != audio_duration_2:
    print("Audio files are not of the same length or sampling rate!")
    exit()

# Calculate the cosine distance between the audio signals
similarity = 1 - cosine(audio_array_1, audio_array_2)

print("Similarity: ", similarity)
