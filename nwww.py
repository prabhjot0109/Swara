import tkinter as tk

# Initialize the Tkinter GUI
root = tk.Tk()

# Set the title of the window
root.title("Word and Sentence Display")

# Set the size of the window
root.geometry("300x150")

# Create a label to display the word
word_label = tk.Label(root, text="Word")
word_label.pack()

# Create a function to display the sentence
def display_sentence():
    # Clear the label displaying the word
    word_label.config(text="")
    # Display the sentence in the same label
    sentence_label.config(text="This is a sentence")
    # Enable the back button
    back_button.config(state=tk.NORMAL)
    # Disable the next button
    next_button.config(state=tk.DISABLED)

# Create a label to display the sentence
sentence_label = tk.Label(root, text="")
sentence_label.pack()

# Create a button to display the sentence
next_button = tk.Button(root, text="Next", command=display_sentence)
next_button.pack()

# Create a function to display the word
def display_word():
    # Clear the label displaying the sentence
    sentence_label.config(text="")
    # Display the word in the same label
    word_label.config(text="Word")
    # Disable the back button
    back_button.config(state=tk.DISABLED)
    # Enable the next button
    next_button.config(state=tk.NORMAL)

# Create a button to display the word
back_button = tk.Button(root, text="Back", command=display_word, state=tk.DISABLED)
back_button.pack()

# Start the Tkinter event loop
root.mainloop()
