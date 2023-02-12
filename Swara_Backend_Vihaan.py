import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy as npy

time = 0

def getSpecs(file):
    global time
    file_spec = wave.open(file, 'rb')
    
    sample_freq = file_spec.getframerate()
    frames = file_spec.getnframes()
    signal_wave = file_spec.readframes(-1)
    file_spec.close()
    time = frames / sample_freq

    #For 1 channel : int16 and for 2 : int32
    arr = npy.frombuffer(signal_wave, dtype=npy.int16)
    times = npy.linspace(0, time, num=frames)

    return arr,times

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

audio = pyaudio.PyAudio()

user_file = "user.wav"

record = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER)
    
user_choice= int(input("press 1 to start recording the song you want to compare.\npress 2 to upload the song you want to compare."))

if (user_choice==1):
    print('Start Recording')
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

    specimen = wave.open(user_file, 'wb')
    specimen.setnchannels(CHANNELS)
    specimen.setsampwidth(audio.get_sample_size(FORMAT))
    specimen.setframerate(RATE)
    specimen.writeframes(b''.join(frames))
    specimen.close()

    user_arr,user_times = getSpecs(user_file)

else:
    file_path_user = input('Enter a user file path: ')
    user_arr,user_times = getSpecs(file_path_user)

#ORIGINAL FILE EXPERIMENTAL CODE
#user input of original file

org_file_path = input('Enter a org file path: ')
org_arr,org_times = getSpecs(org_file_path)

plt.figure(figsize=(15, 5))
plt.plot(user_times, user_arr , color = 'pink')
plt.plot(org_times,org_arr, color = 'paleturquoise')
plt.ylabel('Sound Wave')
plt.xlabel('Time (s)')
plt.xlim(0, time)
plt.title('Graph of the specimen and original song')
plt.legend()
plt.show()
