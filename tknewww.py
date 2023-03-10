import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Create a Tkinter window
root = tk.Tk()
root.geometry('600x400')

# Create a Matplotlib figure
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('My plot')

# Embed the figure in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Add a toolbar with save and zoom options
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Add a button to save the figure
def save_figure():
    fig.savefig('my_figure.png')

save_button = tk.Button(root, text='Save Figure', command=save_figure)
save_button.pack()

# Start the Tkinter event loop
tk.mainloop()
