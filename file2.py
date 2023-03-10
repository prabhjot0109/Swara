import tkinter as tk
from tkinter import filedialog
import Swara_Backend

def get_file_path_1():
    file_path_1 = filedialog.askopenfilename()
    label_file_1.config(text=file_path_1)

def get_file_path_2():
    file_path_2 = filedialog.askopenfilename()
    label_file_2.config(text=file_path_2)

def process_files():
    file_path_1 = label_file_1.cget("text")
    file_path_2 = label_file_2.cget("text")
    Swara_Backend.process_files(file_path_1, file_path_2)
    result_window = tk.Toplevel(root)
    result_label = tk.Label(result_window, text=f"File 1: {file_path_1}\nFile 2: {file_path_2}")
    result_label.pack()

root = tk.Tk()

label_file_1 = tk.Label(root, text="")
label_file_1.pack()

button_1 = tk.Button(root, text="Select File 1", command=get_file_path_1)
button_1.pack()

label_file_2 = tk.Label(root, text="")
label_file_2.pack()

button_2 = tk.Button(root, text="Select File 2", command=get_file_path_2)
button_2.pack()

process_button = tk.Button(root, text="Process Files", command=process_files)
process_button.pack()

root.mainloop()
