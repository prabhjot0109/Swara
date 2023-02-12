import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pyaudio
import wave
import numpy as np
from tkinter import *

#Python Backend Programming for file input and graph comparision.
def Backend(user_p,org_p,text):
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
        frames_per_buffer=FRAMES_PER_BUFFER
    )

    #user_choice = int(input("Enter your choice : "))


    # if (user_choice==1):      
    #     print('START RECORDING')
    #     seconds = 8
    #     frames = []
    #     second_tracking = 0
    #     second_count = 0
    #     for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
    #             data = record.read(FRAMES_PER_BUFFER)
    #             frames.append(data)
    #             second_tracking += 1

    #             if second_tracking == RATE/FRAMES_PER_BUFFER:
    #                     second_count += 1
    #                     second_tracking = 0
    #                     print(f'Time Left: {seconds - second_count} seconds')


    #     record.stop_stream()
    #     record.close()
    #     audio.terminate()

    #     specimen = wave.open('user.wav', 'wb')
    #     specimen.setnchannels(CHANNELS)
    #     specimen.setsampwidth(audio.get_sample_size(FORMAT))
    #     specimen.setframerate(RATE)
    #     specimen.writeframes(b''.join(frames))
    #     specimen.close()

    #     file_spec = wave.open('user.wav', 'rb')
    #     sample_freq = file_spec.getframerate()
    #     frames = file_spec.getnframes()
    #     signal_wave = file_spec.readframes(-1)
    #     file_spec.close()


    # file_path1 = input('Enter Recorded file path: ')
    file_spec = wave.open(user_p, 'rb')
    sample_freq = file_spec.getframerate()
    frames = file_spec.getnframes()
    signal_wave = file_spec.readframes(-1)

    file_spec.close()

    time = frames / sample_freq

    # User File Graph
    user_arr = np.frombuffer(signal_wave, dtype=np.int16)
    user_times = np.linspace(0, time, num=frames)

    #ORIGINAL FILE EXPERIMENTAL CODE

    #user input of original file
    # file_path = input('Enter Original file path: ')
    file_real = wave.open(org_p, 'rb')
    sample_freq = file_real.getframerate()
    frames = file_real.getnframes()
    signal_wave = file_real.readframes(-1)

    file_real.close()

    time = frames / sample_freq

    org_arr = np.frombuffer(signal_wave, dtype=np.int16)
    org_times = np.linspace(0, time, num=frames)

    # --------- Plotting Graph ----------
    fig =  Figure(figsize=(15, 5))
    ax = fig.add_subplot(111)

    ax.plot(user_times, user_arr , color = 'red')
    ax.plot(org_times,org_arr, color = 'orange')

    plt.ylabel('Sound Wave')
    plt.xlabel('Time (s)')
    plt.xlim(0, time)
    plt.title('Graph of the specimen and original song')
    
    # Compare pitch
    org_pitch = np.mean(np.abs(np.diff(org_arr)))
    user_pitch = np.mean(np.abs(np.diff(org_times)))

    if org_pitch > user_pitch:
        text.config(text=text.cget("text") + "\nFile 1 has higher pitch.")
    
    elif org_pitch < user_pitch:
        text.config(text=text.cget("text") + "\nFile 2 has higher pitch.")
    
    else:
        text.config(text=text.cget("text") + "\nBoth files have the same pitch.")

    return fig