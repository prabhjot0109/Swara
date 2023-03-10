import wave
import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

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

# Set the parameters for MFCC extraction
n_mfcc = 13
frame_length = int(0.02 * sampling_rate_1)
hop_length = int(frame_length / 2)

# Compute the MFCC features for each audio file
mfcc_1 = compute_mfcc(audio_array_1, sampling_rate_1, n_mfcc, frame_length, hop_length)
mfcc_2 = compute_mfcc(audio_array_2, sampling_rate_2, n_mfcc, frame_length, hop_length)

# Compute the DTW distance and similarity score
distance, path = fastdtw(mfcc_1.T, mfcc_2.T, dist=euclidean)
similarity = 1 / (1 + distance)

print("Similarity: ", similarity)

def compute_mfcc(audio_data, sampling_rate, n_mfcc, frame_length, hop_length):
    """
    Compute the Mel-frequency cepstral coefficients (MFCCs) for an audio signal.
    """
    # Pre-emphasis filter
    pre_emphasis = 0.97
    emphasized_signal = np.append(audio_data[0], audio_data[1:] - pre_emphasis * audio_data[:-1])

    # Compute the power spectrum
    window = np.hamming(frame_length)
    power_spectrum = np.abs(np.square(np.fft.rfft(emphasized_signal * window, n=frame_length)))

    # Compute the Mel filterbank
    mel_filterbank = librosa.filters.mel(sampling_rate, n_fft=frame_length, n_mels=n_mfcc)

    # Compute the logarithmic Mel power spectrum
    log_mel_spectrum = np.log10(np.dot(power_spectrum, mel_filterbank.T) + 1e-20)

    # Compute the MFCCs
    mfcc = librosa.feature.mfcc(S=log_mel_spectrum, n_mfcc=n_mfcc, hop_length=hop_length)
    return mfcc

