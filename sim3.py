import wave
import numpy as np
from scipy.spatial.distance import cosine
from pyAudioAnalysis import audioBasicIO, chroma

# Load the audio files
audio_file_1 = "path/to/audio/file1.wav"
audio_file_2 = "path/to/audio/file2.wav"

# Open the audio files and read the data
with wave.open(audio_file_1, 'rb') as f:
    params_1 = f.getparams()
    audio_data_1 = f.readframes(params_1[3])
    sampling_rate_1 = f.getframerate()

with wave.open(audio_file_2, 'rb') as f:
    params_2 = f.getparams()
    audio_data_2 = f.readframes(params_2[3])
    sampling_rate_2 = f.getframerate()

# Convert the audio data to numpy arrays
audio_array_1 = np.frombuffer(audio_data_1, dtype=np.int16)
audio_array_2 = np.frombuffer(audio_data_2, dtype=np.int16)

# Set the parameters for chroma feature extraction
win_size = 1.0
step_size = 1.0

# Compute the chroma features for each audio file
chroma_1 = chroma.chroma_features(audio_array_1, sampling_rate_1, win_size, win_size, step_size)[0]
chroma_2 = chroma.chroma_features(audio_array_2, sampling_rate_2, win_size, win_size, step_size)[0]

# Compute the cosine distance and similarity score
distance = cosine(chroma_1.flatten(), chroma_2.flatten())
similarity = 1 - distance

print("Similarity: ", similarity)
