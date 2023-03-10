import wave
import numpy as np
import aubio

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
n_fft = 2048
hop_size = 512

# Create the pitch object and set its parameters
pitch_o = aubio.pitch("yin", n_fft, hop_size, sampling_rate_1)
pitch_o.set_unit("midi")
pitch_o.set_silence(-40)

# Compute the chroma features for each audio file
chroma_1 = np.zeros(12)
chroma_2 = np.zeros(12)

for i in range(0, len(audio_array_1), hop_size):
    pitch = pitch_o(audio_array_1[i:i+hop_size])[0]
    if pitch != 0:
        note = int(round(aubio.midi2note(pitch)))
        chroma_1[note % 12] += 1

for i in range(0, len(audio_array_2), hop_size):
    pitch = pitch_o(audio_array_2[i:i+hop_size])[0]
    if pitch != 0:
        note = int(round(aubio.midi2note(pitch)))
        chroma_2[note % 12] += 1

# Compute the cosine distance and similarity score
distance = np.linalg.norm(chroma_1 - chroma_2)
similarity = 1 / (1 + distance)

print("Similarity: ", similarity)
