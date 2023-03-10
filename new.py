import tkinter as tk

def show_previous_window(current_window, previous_window):
    current_window.withdraw()
    previous_window.deiconify()

def create_window():
    # Create the first window
    window1 = tk.Tk()

    # Create a button to go to the second window
    button1 = tk.Button(window1, text="Go to Window 2", command=lambda: show_previous_window(window1, window2))
    button1.pack()

    # Start the event loop for the first window
    window1.mainloop()

    # Create the second window
    window2 = tk.Toplevel()

    # Create a button to go back to the first window
    button2 = tk.Button(window2, text="Go back to Window 1", command=lambda: show_previous_window(window2, window1))
    button2.pack()

    # Start the event loop for the second window
    window2.mainloop()

# Call the create_window function to start the application
create_window()
