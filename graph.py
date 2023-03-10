import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
root = tk.Tk()
root.title("Matplotlib graph in Tkinter GUI")

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

ax.plot(x, y)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
def save():
    fig.savefig('D:\Coding\Swara-master\mygraph.png')

save_button = tk.Button(master=root, text='Save', command=save)
save_button.pack(side=tk.BOTTOM)
tk.mainloop()
