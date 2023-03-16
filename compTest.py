import librosa
import numpy as np

# Load audio files
audio_file_1, sr_1 = librosa.load("Audio/user.wav")
audio_file_2, sr_2 = librosa.load("Audio/user1.wav")

# Compute chroma features for each audio file
chroma_1 = librosa.feature.chroma_cqt(y=audio_file_1, sr=sr_1)
chroma_2 = librosa.feature.chroma_cqt(y=audio_file_2, sr=sr_2)

# Compute the cosine similarities between corresponding chroma features
n_frames = min(chroma_1.shape[1], chroma_2.shape[1])
similarities = np.zeros(n_frames)
for i in range(n_frames):
    similarities[i] = np.dot(chroma_1[:, i], chroma_2[:, i]) / (np.linalg.norm(chroma_1[:, i]) * np.linalg.norm(chroma_2[:, i]))

# Compute the average similarity score
similarity = np.mean(similarities) * 100

print(f"The similarity between the two audio files is {similarity:.2f}%.")
