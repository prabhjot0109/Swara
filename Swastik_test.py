import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy as npy

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

audio = pyaudio.PyAudio()

record = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER)

print()
print()
print("Welcome  to SWARA!")
print()
print("How can I help you!")
print()

user_choice= int(input("press 1 to start recording the song you want to compare.\npress 2 to upload the song you want to compare."))

if (user_choice==1):
    
    print('start recording')
    seconds = 8
    frames = []
    second_tracking = 0
    second_count = 0
    for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
        data = record.read(FRAMES_PER_BUFFER)
        frames.append(data)
        second_tracking += 1
        if second_tracking == RATE/FRAMES_PER_BUFFER:
            second_count += 1
            second_tracking = 0
            print(f'Time Left: {seconds - second_count} seconds')


    record.stop_stream()
    record.close()
    audio.terminate()

    specimen = wave.open('Audio/user.wav', 'wb')
    specimen.setnchannels(CHANNELS)
    specimen.setsampwidth(audio.get_sample_size(FORMAT))
    specimen.setframerate(RATE)
    specimen.writeframes(b''.join(frames))
    specimen.close()

    file_spec = wave.open('Audio/user.wav', 'rb')
    sample_freq = file_spec.getframerate()
    frames = file_spec.getnframes()
    signal_wave = file_spec.readframes(-1)
    file_spec.close()

else:

    file_path1 = input('Enter a user file path: ')
    file_spec = wave.open(file_path1, 'rb')
    sample_freq = file_spec.getframerate()
    frames = file_spec.getnframes()
    signal_wave = file_spec.readframes(-1)
    
    file_spec.close()


time = frames / sample_freq

arr = npy.frombuffer(signal_wave, dtype=npy.int16)
times = npy.linspace(0, time, num=frames)


#ORIGINAL FILE EXPERIMENTAL CODE
#user input of original file

file_path = input('Enter a org file path: ')
file_real = wave.open(file_path, 'rb')
sample_freq = file_real.getframerate()
frames = file_real.getnframes()
signal_wave = file_real.readframes(-1)
file_real.close()
time = frames / sample_freq

# if one channel use int16, if 2 use int32
arr2 = npy.frombuffer(signal_wave, dtype=npy.int16)
times2 = npy.linspace(0, time, num=frames)


plt.figure(figsize=(15, 5))
plt.plot(times, arr , color = 'pink')
plt.plot(times2,arr2, color = 'paleturquoise')
plt.ylabel('Sound Wave')
plt.xlabel('Time (s)')
plt.xlim(0, time)
plt.title('Graph of the specimen and original song')
plt.legend()
plt.show()





