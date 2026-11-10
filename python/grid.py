# A test for making grid in tkinter using python
import tkinter as tk

root = tk.Tk()
# root.overrideredirect(True)

title = tk.Label(root, text='')
title.grid(columnspan=2)

name_label = tk.Label(root, text='What is your name?')
name_label.grid(row=0, column=0)






root.geometry('800x600+300+300')
root.resizable(False, False)

root.mainloop()