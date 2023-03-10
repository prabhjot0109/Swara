# import tkinter as tk
# from tkinter import filedialog
# import Swara_Backend

# def get_file_path():
#     file_path = filedialog.askopenfilename()
#     Swara_Backend.process_file(file_path)

# root = tk.Tk()

# button = tk.Button(root, text="Select File", command=get_file_path)
# button.pack()

# root.mainloop()

# import tkinter as tk
# from tkinter import filedialog
# import Swara_Backend

# def get_file_path_1():
#     file_path_1 = filedialog.askopenfilename()
#     get_file_path_2(file_path_1)

# def get_file_path_2(file_path_1):
#     file_path_2 = filedialog.askopenfilename()
#     Swara_Backend.plot_audio_files(file_path_1, file_path_2)

# root = tk.Tk()

# button_1 = tk.Button(root, text="Select File 1", command=get_file_path_1)
# button_1.pack()

# root.mainloop()


import tkinter as tk
from tkinter import filedialog
import Swara_Backend

def get_file_path_1():
    file_path_1 = filedialog.askopenfilename()
    label_file_1.config(text=file_path_1)

def get_file_path_2():
    file_path_2 = filedialog.askopenfilename()
    label_file_2.config(text=file_path_2)
    plot_audio_files()

def plot_audio_files():
    file_path_1 = label_file_1.cget("text")
    file_path_2 = label_file_2.cget("text")
    Swara_Backend.plot_audio_files(file_path_1, file_path_2)

root = tk.Tk()

label_file_1 = tk.Label(root, text="")
label_file_1.pack()

button_1 = tk.Button(root, text="Select File 1", command=get_file_path_1)
button_1.pack()

label_file_2 = tk.Label(root, text="")
label_file_2.pack()

button_2 = tk.Button(root, text="Select File 2", command=get_file_path_2)
button_2.pack()

root.mainloop()
