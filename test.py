import librosa

# load audio files
y1, sr1 = librosa.load("y2mate.com - Maroon 5   Animals  cover by J Fla.wav")
y2, sr2 = librosa.load("y2mate.com - Maroon 5  Animals Lyrics.wav")

# extract pitch
pitch1 = librosa.estimate_tuning(y=y1, sr=sr1)
pitch2 = librosa.estimate_tuning(y=y2, sr=sr2)

# compare pitch
pitch_diff = (pitch1 - pitch2) * 100

print(pitch_diff)

