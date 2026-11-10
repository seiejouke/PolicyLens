# main program for tkinter
import tkinter as tk
from tkinter import ttk

root = tk.Tk() # venster
label = tk.Label(root, text="Hello World")
label.pack()

button = tk.Button(root, text="Don't press me!")
button.pack()

entry = tk.Entry(root, width=20)
entry.pack()

root.mainloop()