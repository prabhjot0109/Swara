import tkinter as tk

def previous_window():
    current_window.destroy()
    prev_window = tk.Toplevel()
    prev_window.title("Previous Window")
    label = tk.Label(prev_window, text="This is the previous window")
    label.pack()
    button = tk.Button(prev_window, text="Open Current Window", command=current_window)
    button.pack()

def current_window():
    prev_window.destroy()
    current_window = tk.Toplevel()
    current_window.title("Current Window")
    label = tk.Label(current_window, text="This is the current window")
    label.pack()
    button = tk.Button(current_window, text="Open Previous Window", command=previous_window)
    button.pack()

if __name__ == '__main__':
    main_window = tk.Tk()
    main_window.title("Main Window")
    prev_window = tk.Toplevel()
    prev_window.title("Previous Window")
    label = tk.Label(prev_window, text="This is the previous window")
    label.pack()
    button = tk.Button(prev_window, text="Open Current Window", command=current_window)
    button.pack()
    main_window.mainloop()
